from abc import ABC, abstractmethod


class BaseWorker(ABC):

    @abstractmethod
    def work(self):
        ...


class Worker(BaseWorker):

    def work(self):
        print("I'm working!!")


class SuperWorker(BaseWorker):

    def work(self):
        print("I work very hard!!!")


class UltimateWorker(BaseWorker):

    def work(self):
        print("I work very very very hard!!!")


class Manager:

    def __init__(self):
        self.worker = None

    def set_worker(self, worker):
        if not isinstance(worker, BaseWorker):
            raise TypeError(f'`worker` must be of type {BaseWorker}')

        self.worker = worker

    def manage(self):
        if self.worker is not None:
            self.worker.work()





worker = Worker()
manager = Manager()
manager.set_worker(worker)
manager.manage()

super_worker = SuperWorker()
ultimate_worker = UltimateWorker()
try:
    manager.set_worker(super_worker)
    manager.manage()
    manager.set_worker(ultimate_worker)
    manager.manage()
except AssertionError:
    print("manager fails to support super_worker....")
