#-*-coding:utf8-*-
import multiprocessing

class MultiProcessHelper(object):
    def __init__(self,processes):
        self._pool = multiprocessing.Pool(processes = processes)
        self._taskLock = multiprocessing.Condition(multiprocessing.Lock())
        self._result = []

    def apply_async(self, task, args = None):
        self._taskLock.acquire()
        result = self._pool.apply_async(task,(args,))
        self._taskLock.release()

    def terminate(self):
        self._pool.terminate()
