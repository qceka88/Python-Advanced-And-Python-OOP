from unittest import main, TestCase


class TestIntegerList(TestCase):

    def setUp(self) -> None:
        self.list = IntegerList(1, 4, 5, 6, 7, 8, 9)

    def test_initialisation(self):
        init_list = [1, 4, 5, 6, 7, 8, 9]
        self.assertEqual(init_list, self.list._IntegerList__data)

        test_list = IntegerList(1, "a", 5.5, [1, 2], 4, 5, 6, "a1", 7, 8, 9)
        self.assertEqual(init_list, test_list._IntegerList__data)

        self.assertEqual(init_list, self.list.get_data())

    def test_add_for_invalid_element_raises_value_error(self):
        invalid_elements = ["a1", 5.5, [1, 2], {}, (1,), "1", "5.5"]

        for el in invalid_elements:
            with self.assertRaises(ValueError) as ve:
                self.list.add(el)

            self.assertEqual("Element is not Integer", str(ve.exception))

    def test_add_for_valid_element(self):
        expected_result = [1, 4, 5, 6, 7, 8, 9, 3]
        result = self.list.add(3)

        self.assertEqual(expected_result, result)
        self.assertEqual(3, self.list._IntegerList__data[-1])

    def test_remove_index_for_invalid_index(self):
        with self.assertRaises(IndexError) as ie:
            self.list.remove_index(7)

        self.assertEqual("Index is out of range", str(ie.exception))

    def test_remove_index_for_valid_input(self):
        result = self.list.remove_index(6)
        self.assertEqual(9, result)

        expected_data = [1, 4, 5, 6, 7, 8]
        self.assertEqual(expected_data, self.list._IntegerList__data)

    def test_get_method_raises_index_error(self):
        with self.assertRaises(IndexError) as ie:
            self.list.get(7)

        self.assertEqual("Index is out of range", str(ie.exception))

    def test_get_method_valid_input(self):
        result = self.list.get(5)
        self.assertEqual(8, result)

    def test_insert_method_raises_invalid_index(self):
        with self.assertRaises(IndexError) as ie:
            self.list.insert(7, 5)

        self.assertEqual("Index is out of range", str(ie.exception))

    def test_insert_method_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.list.insert(5, "5")

        self.assertEqual("Element is not Integer", str(ve.exception))

    def test_insert_method_for_valid_input(self):
        self.list.insert(5, 11)

        test_list = [1, 4, 5, 6, 7, 11, 8, 9]
        self.assertEqual(test_list, self.list.get_data())

    def test_get_biggest(self):
        result = self.list.get_biggest()
        self.assertEqual(9, result)

    def test_get_index(self):
        result = self.list.get_index(6)
        self.assertEqual(3, result)


if __name__ == '__main__':
    main()

#################################### TASK CONDITION ############################
'''
                            3.	List
You are provided with a class IntegerList. It should only store integers. The initial integers 
should be set by the constructor. They are stored as a list. IntegerList has a functionality to add, 
remove_index, get, insert, get the biggest number, and get the index of an element. 
Your task is to test the class.
Note: You are not allowed to change the structure of the provided code
Constraints
•	add operation, should add an element and returns the list.
o	If the element is not an integer, a ValueError is thrown
•	remove_index operation removes the element on that index and returns it.
o	If the index is out of range, an IndexError is thrown
•	__init__ should only take integers, and store them
•	get should return the specific element
o	If the index is out of range, an IndexError is thrown
•	insert
o	If the index is out of range, IndexError is thrown
o	If the element is not an integer, ValueError is thrown
•	get_biggest
•	get_index
Hint
Do not forget to test the constructor

 '''


# Code to test
class IntegerList:
    def __init__(self, *args):
        self.__data = []
        for x in args:
            if type(x) == int:
                self.__data.append(x)

    def get_data(self):
        return self.__data

    def add(self, element):
        if not type(element) == int:
            raise ValueError("Element is not Integer")
        self.get_data().append(element)
        return self.get_data()

    def remove_index(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        a = self.get_data()[index]
        del self.get_data()[index]
        return a

    def get(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        return self.get_data()[index]

    def insert(self, index, el):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        elif not type(el) == int:
            raise ValueError("Element is not Integer")

        self.get_data().insert(index, el)

    def get_biggest(self):
        a = sorted(self.get_data(), reverse=True)
        return a[0]

    def get_index(self, el):
        return self.get_data().index(el)
