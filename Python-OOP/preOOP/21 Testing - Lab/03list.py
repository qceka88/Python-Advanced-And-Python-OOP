
from unittest import main, TestCase


class TestIntegerList(TestCase):

    def setUp(self):
        self.list = IntegerList({"1": 1}, 1, "a", 2.5, 2, [1, 2, 3], 3)

    def test_initialisation_is_correct(self):
        self.assertEqual([1, 2, 3], self.list._IntegerList__data)

    def test_get_data_method(self):
        self.assertEqual([1, 2, 3], self.list.get_data())

    def test_add_method_for_wrong_type_of_data(self):
        with self.assertRaises(ValueError) as ve:
            self.list.add(1.5)

        self.assertEqual("Element is not Integer", str(ve.exception))

    def test_add_method_for_successful_added_element(self):
        result = self.list.add(4)

        self.assertEqual([1, 2, 3, 4], self.list._IntegerList__data)
        self.assertEqual(self.list._IntegerList__data, result)

    def test_remove_index_method_for_invalid_index(self):
        with self.assertRaises(IndexError) as ve:
            self.list.remove_index(3)

        self.assertEqual("Index is out of range", str(ve.exception))

    def test_remove_index_method_for_proper_removing(self):
        result = self.list.remove_index(1)

        self.assertEqual(2, result)
        self.assertEqual([1, 3], self.list._IntegerList__data)

    def test_get_method_for_invalid_index(self):
        with self.assertRaises(IndexError) as ve:
            self.list.get(3)

        self.assertEqual("Index is out of range", str(ve.exception))

    def test_get_method_for_proper_return_data(self):
        result = self.list.get(2)
        self.assertEqual(3, result)

    def test_insert_method_for_invalid_index(self):
        with self.assertRaises(IndexError) as ie:
            self.list.insert(3, 3)

        self.assertEqual("Index is out of range", str(ie.exception))

    def test_insert_method_for_invalid_element(self):
        with self.assertRaises(ValueError) as ve:
            self.list.insert(0, "3")

        self.assertEqual("Element is not Integer", str(ve.exception))

    def test_insert_method_for_proper_inserting_element(self):
        self.list.insert(2, 4)

        self.assertEqual([1, 2, 4, 3], self.list._IntegerList__data)

    def test_get_biggest_method_for_returning_number(self):
        result = self.list.get_biggest()

        self.assertEqual(3, result)

    def test_get_index_method(self):
        result = self.list.get_index(3)

        self.assertEqual(2, result)


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


