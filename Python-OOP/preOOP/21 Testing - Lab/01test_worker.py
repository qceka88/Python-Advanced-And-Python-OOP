
from unittest import main, TestCase


class TestWorker(TestCase):

    def setUp(self) -> None:
        self.worker = Worker("TestName", 1000, 100)

    def test_is_initialisation_correct(self):
        self.assertEqual("TestName", self.worker.name)
        self.assertEqual(1000, self.worker.salary)
        self.assertEqual(100, self.worker.energy)
        self.assertEqual(0, self.worker.money)

    def test_worker_with_insufficient_energy_raises_exception(self):
        self.worker.energy = 0
        with self.assertRaises(Exception) as ex:
            self.worker.work()

        self.assertEqual('Not enough energy.', str(ex.exception))

    def test_work_method_for_increasing_money_after_work(self):
        self.worker.work()
        self.assertEqual(1000, self.worker.money)

    def test_work_method_for_decreasing_energy_after_work(self):
        self.worker.work()
        self.assertEqual(99, self.worker.energy)

    def test_rest_method_for_increasing_energy_after_rest(self):
        self.worker.rest()
        self.assertEqual(101, self.worker.energy)

    def test_get_info_method(self):
        self.assertEqual("TestName has saved 0 money.", self.worker.get_info())


if __name__ == "__main__":
    main()


#################################### TASK CONDITION ############################
'''
                      1.	Test Worker
Load provided skeleton in the IDE you use. Add new project Tests.


 '''

# Code to test
class Worker:

    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception('Not enough energy.')

        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return f'{self.name} has saved {self.money} money.'


'''

Create a class WorkerTests
In judge you need to submit just the WokerTests class, with the unittest module imported.
Create the following tests:
•	Test if the worker is initialized with the correct name, salary, and energy
•	Test if the worker's energy is incremented after the rest method is called
•	Test if an error is raised if the worker tries to work with negative energy or equal to 0
•	Test if the worker's money is increased by his salary correctly after the work method is called
•	Test if the worker's energy is decreased after the work method is called	
•	Test if the get_info method returns the proper string with correct values

'''
