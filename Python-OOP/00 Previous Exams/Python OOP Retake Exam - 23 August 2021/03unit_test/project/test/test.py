from project.library import Library
from unittest import main, TestCase


class TestLibrary(TestCase):

    def setUp(self):
        self.library = Library("Yambol")
        self.library02 = Library("Sliven")
        self.library02.books_by_authors = {"author01": ["book01", "book02"], "author02": ["book01", "book02"]}
        self.library02.readers = {"reader01": [], "reader02": [], "reader03": []}

    def test_initialisation_is_correct(self):
        self.assertEqual("Yambol", self.library.name)
        self.assertEqual({}, self.library.books_by_authors)
        self.assertEqual({}, self.library.readers)

    def test_name_setter_for_invalid_name(self):
        with self.assertRaises(ValueError) as ve:
            test = Library("")

        self.assertEqual("Name cannot be empty string!", str(ve.exception))

    def test_add_book(self):
        books = {"author01": ["book01", "book02"], "author02": ["book01", "book02"]}

        for author, titles in books.items():
            for title in titles:
                self.library.add_book(author, title)

        self.assertEqual(books, self.library.books_by_authors)

    def test_add_reader_valid_data(self):
        readers = {"reader01": [], "reader02": [], "reader03": []}
        for r in readers:
            self.library.add_reader(r)

        self.assertEqual(readers, self.library.readers)

    def test_add_rear_for_existing_reader(self):
        result = self.library02.add_reader("reader02")
        self.assertEqual("reader02 is already registered in the Sliven library.", result)

    def test_rent_book_for_unregistered_reader(self):
        result = self.library02.rent_book("reader04", "author01", "book01")
        self.assertEqual("reader04 is not registered in the Sliven Library.", result)

    def test_rent_book_for_non_existing_author(self):
        result = self.library02.rent_book("reader01", "author100", "book01")
        self.assertEqual("Sliven Library does not have any author100's books.", result)

    def test_rent_book_for_non_existing_title(self):
        result = self.library02.rent_book("reader01", "author01", "book100")
        self.assertEqual("""Sliven Library does not have author01's "book100".""", result)

    def test_rent_book_for_valid_data(self):
        self.library02.rent_book("reader02", "author02", "book01")

        expected_readers = {"reader01": [], "reader02": [{"author02": "book01"}], "reader03": []}
        expected_books_by_authors = {"author01": ["book01", "book02"], "author02": ["book02"]}

        self.assertEqual(expected_readers, self.library02.readers)
        self.assertEqual(expected_books_by_authors, self.library02.books_by_authors)


if __name__ == '__main__':
    main()
