from unittest import main, TestCase


class TestCat(TestCase):

    def setUp(self) -> None:
        self.cat = Cat("Test")

    def test_initialisation_is_correct(self):
        self.assertEqual("Test", self.cat.name)
        self.assertFalse(self.cat.fed)
        self.assertFalse(self.cat.sleepy)
        self.assertEqual(0, self.cat.size)

    def test_eat_raises_exception(self):
        self.cat.fed = True

        with self.assertRaises(Exception) as ex:
            self.cat.eat()

        self.assertEqual('Already fed.', str(ex.exception))

    def test_eat_valid_work(self):
        self.cat.eat()

        self.assertEqual(1, self.cat.size)
        self.assertTrue(self.cat.fed)
        self.assertTrue(self.cat.sleepy)

    def test_sleep_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.cat.sleep()

        self.assertEqual('Cannot sleep while hungry', str(ex.exception))

    def test_sleep_for_proper_working(self):
        self.cat.fed = True
        self.cat.sleepy = True
        self.cat.sleep()

        self.assertFalse(self.cat.sleepy)


if __name__ == '__main__':
    main()


#################################### TASK CONDITION ############################
'''
                               2.	Test Cat

 '''

# Code to test
class Cat:

    def __init__(self, name):
        self.name = name
        self.fed = False
        self.sleepy = False
        self.size = 0

    def eat(self):
        if self.fed:
            raise Exception('Already fed.')

        self.fed = True
        self.sleepy = True
        self.size += 1

    def sleep(self):
        if not self.fed:
            raise Exception('Cannot sleep while hungry')

        self.sleepy = False


'''

Create a class CatTests
In judge you need to submit just the CatTests class, with the unitttest module imported.
Create the following tests:
•	Cat's size is increased after eating
•	Cat is fed after eating
•	Cat cannot eat if already fed, raises an error
•	Cat cannot fall asleep if not fed, raises an error
•	Cat is not sleepy after sleeping
Hints
Follow the logic of the previous problem


'''
