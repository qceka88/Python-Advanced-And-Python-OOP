from abc import ABC, abstractmethod
import time


class WorkAction(ABC):

    @abstractmethod
    def work(self):
        ...


class EatAction(ABC):

    @abstractmethod
    def eat(self):
        ...


class Worker(WorkAction, EatAction):

    def work(self):
        print("I'm normal worker. I'm working.")

    def eat(self):
        print("Lunch break....(5 secs)")
        time.sleep(5)


class SuperWorker(WorkAction, EatAction):

    def work(self):
        print("I'm super worker. I work very hard!")

    def eat(self):
        print("Lunch break....(3 secs)")
        time.sleep(3)


class Robot(WorkAction):

    def work(self):
        print("I'm a robot. I'm working....")


class LazyWorker(WorkAction, EatAction):

    def work(self):
        print("I`m best worker, but first I need to eat")
        time.sleep(5)

    def eat(self):
        print("Finally after that heavy work")
        time.sleep(3)


class MainManager(ABC):

    def __init__(self):
        self.worker = None

    @abstractmethod
    def set_worker(self, worker):
        ...


class BreakManager(MainManager):

    def set_worker(self, worker):
        assert isinstance(worker, EatAction), f"`worker` must be of type {worker}"

        self.worker = worker

    def lunch_break(self):
        self.worker.eat()


class WorkManager(MainManager):

    def set_worker(self, worker):
        assert isinstance(worker, WorkAction), f"`worker` must be of type {worker}"

        self.worker = worker

    def manage(self):
        self.worker.work()


work_manager = WorkManager()
break_manager = BreakManager()
work_manager.set_worker(Worker())
break_manager.set_worker(Worker())
work_manager.manage()
break_manager.lunch_break()

work_manager.set_worker(SuperWorker())
break_manager.set_worker(SuperWorker())
work_manager.manage()
break_manager.lunch_break()

work_manager.set_worker(Robot())
work_manager.manage()
try:
    break_manager.set_worker(Robot())
    break_manager.lunch_break()
except:
    pass

work_manager.set_worker(LazyWorker())
break_manager.set_worker(LazyWorker())
work_manager.manage()
break_manager.lunch_break()

#################################### TASK CONDITION ############################
'''
                            2.	Workers - Updated
You are provided with a code on which you have to apply the 
ISP (Interface Segregation Principle) by splitting the Worker class into two classes 
(Workable and Eatable), so the Robot class no longer needs to implement the eat method


 '''

# Code to fix
from abc import ABCMeta, abstractmethod
import time


class AbstractWorker:
    __metaclass__ = ABCMeta

    @abstractmethod
    def work(self):
        pass

    @abstractmethod
    def eat(self):
        pass


class Worker(AbstractWorker):

    def work(self):
        print("I'm normal worker. I'm working.")

    def eat(self):
        print("Lunch break....(5 secs)")
        time.sleep(5)


class SuperWorker(AbstractWorker):

    def work(self):
        print("I'm super worker. I work very hard!")

    def eat(self):
        print("Lunch break....(3 secs)")
        time.sleep(3)


class Manager:

    def __init__(self):
        self.worker = None

    def set_worker(self, worker):
        assert isinstance(worker, AbstractWorker), "`worker` must be of type {}".format(AbstractWorker)

        self.worker = worker

    def manage(self):
        self.worker.work()

    def lunch_break(self):
        self.worker.eat()


class Robot(AbstractWorker):

    def work(self):
        print("I'm a robot. I'm working....")

    def eat(self):
        print("I don't need to eat....")


manager = Manager()
manager.set_worker(Worker())
manager.manage()
manager.lunch_break()

manager.set_worker(SuperWorker())
manager.manage()
manager.lunch_break()

manager.set_worker(Robot())
manager.manage()
manager.lunch_break()

'''

_______________________________________________
Example

Test Code	(no input data in this task)


work_manager = WorkManager()
break_manager = BreakManager()
work_manager.set_worker(Worker())
break_manager.set_worker(Worker())
work_manager.manage()
break_manager.lunch_break()

work_manager.set_worker(SuperWorker())
break_manager.set_worker(SuperWorker())
work_manager.manage()
break_manager.lunch_break()

work_manager.set_worker(Robot())
work_manager.manage()
try:
    break_manager.set_worker(Robot())
    break_manager.lunch_break()
except:
    pass


Output

I'm normal worker. I'm working.
Lunch break....(5 secs)
I'm super worker. I work very hard!
Lunch break....(3 secs)
I'm a robot. I'm working....


'''
