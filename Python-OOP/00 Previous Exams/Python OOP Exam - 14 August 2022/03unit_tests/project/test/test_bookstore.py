from project.bookstore import Bookstore
from unittest import main, TestCase


class TestStore(TestCase):

    def setUp(self) -> None:
        self.store = Bookstore(5)
        self.store02 = Bookstore(30)
        self.store02.availability_in_store_by_book_titles = {"book01": 5, "book02": 10, "book03": 7}

    def test_initialisation_is_correct(self):
        self.assertEqual(5, self.store.books_limit)
        self.assertEqual({}, self.store.availability_in_store_by_book_titles)
        self.assertEqual(0, self.store._Bookstore__total_sold_books)

    def test_books_limit_setter(self):
        with self.assertRaises(ValueError) as ve:
            test = Bookstore(0)

        self.assertEqual("Books limit of 0 is not valid", str(ve.exception))

        with self.assertRaises(ValueError) as ve:
            test = Bookstore(-1)

        self.assertEqual("Books limit of -1 is not valid", str(ve.exception))

    def test__len__(self):
        result = self.store.__len__()
        self.assertEqual(0, result)

        result02 = len(self.store02)
        self.assertEqual(22, result02)

    def test_receive_book_limit_reached_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.store02.receive_book("book04", 10)

        self.assertEqual("Books limit is reached. Cannot receive more books!", str(ex.exception))

    def test_receive_book_enough_space(self):
        result = self.store02.receive_book("book02", 5)
        self.assertEqual("15 copies of book02 are available in the bookstore.", result)

        self.store.receive_book("book01", 3)
        self.store.receive_book("book01", 1)
        self.assertEqual(4, self.store.availability_in_store_by_book_titles["book01"])

    def test_sell_book_for_non_existing_book_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.store.sell_book("test01", 4)

        self.assertEqual("Book test01 doesn't exist!", str(ex.exception))

    def test_sell_book_for_insufficient_books_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.store02.sell_book("book02", 11)

        self.assertEqual("book02 has not enough copies to sell. Left: 10", str(ex.exception))

    def test_sell_book_for_successfully_sell_book(self):
        books_for_sale = {"book01": 5, "book02": 5, "book03": 2}

        for book, quantity in books_for_sale.items():
            result = self.store02.sell_book(book, quantity)
            self.assertEqual(f"Sold {quantity} copies of {book}", result)

        expected_result = {"book01": 0, "book02": 5, "book03": 5}
        self.assertEqual(expected_result, self.store02.availability_in_store_by_book_titles)
        self.assertEqual(12, self.store02.total_sold_books)
        self.assertEqual(12, self.store02._Bookstore__total_sold_books)

    def test__str__(self):
        books_for_sale = {"book01": 4, "book02": 5, "book03": 2}
        [self.store02.sell_book(book, quantity) for book, quantity in books_for_sale.items()]

        books = " - book01: 1 copies\n - book02: 5 copies\n - book03: 5 copies"
        expected_result = f"Total sold books: 11\nCurrent availability: 11\n{books}"
        expected_result02 = "Total sold books: 0\nCurrent availability: 0"

        self.assertEqual(expected_result, str(self.store02))
        self.assertEqual(expected_result02, str(self.store))


if __name__ == '__main__':
    main()
