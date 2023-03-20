from abc import ABC, abstractmethod


class BaseClassWorker(ABC):

    @abstractmethod
    def work(self):
        ...


class Worker(BaseClassWorker):

    def work(self):
        print("I'm working!!")


class SuperWorker(BaseClassWorker):

    def work(self):
        print("I work very hard!!!")

class Manager:

    def __init__(self):
        self.worker = None

    def set_worker(self, worker):
        assert isinstance(worker, BaseClassWorker), f'`worker` must be of type {worker}'

        self.worker = worker

    def manage(self):
        if self.worker is not None:
            self.worker.work()



# worker = Worker()
# manager = Manager()
# manager.set_worker(worker)
# manager.manage()
#
# super_worker = SuperWorker()
# try:
#     manager.set_worker(super_worker)
# except AssertionError:
#     print("manager fails to support super_worker....")
#
#
worker = Worker()
manager = Manager()
manager.set_worker(worker)
manager.manage()

super_worker = SuperWorker()
try:
    manager.set_worker(super_worker)
    manager.manage()
except AssertionError:
    print("manager fails to support super_worker....")



#################################### TASK CONDITION ############################
'''
            1.	Workers
You are provided with a code on which you have to apply the DIP (Dependency Inversion Principle) 
so that when adding new worker classes, the Manager class will work properly.

 '''

# Code to fix
class Worker:

    def work(self):
        print("I'm working!!")


class Manager:

    def __init__(self):
        self.worker = None

    def set_worker(self, worker):
        assert isinstance(worker, Worker), '`worker` must be of type {}'.format(Worker)

        self.worker = worker

    def manage(self):
        if self.worker is not None:
            self.worker.work()

class SuperWorker:

    def work(self):
        print("I work very hard!!!")



worker = Worker()
manager = Manager()
manager.set_worker(worker)
manager.manage()

super_worker = SuperWorker()
try:
    manager.set_worker(super_worker)
except AssertionError:
    print("manager fails to support super_worker....")


'''

_______________________________________________
Example

Test Code	(no input data in this task)


worker = Worker()
manager = Manager()
manager.set_worker(worker)
manager.manage()

super_worker = SuperWorker()
try:
    manager.set_worker(super_worker)
    manager.manage()
except AssertionError:
    print("manager fails to support super_worker....")

Output

I'm working!!
I work very hard!!!




'''
