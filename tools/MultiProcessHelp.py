#-*-coding:utf8-*-
import multiprocessing

class MultiProcessHelper(object):
    def __init__(self,processes):
        self._pool = multiprocessing.Pool(processes)
        self._taskLock = multiprocessing.Condition(multiprocessing.Lock())
        self._result = []

    def async(self,task,args = None):
        self._taskLock.acquire()
        result = self._pool.apply_async(task,args)
        self._taskLock.release()


    def join(self):
        self._pool.close()
        self._pool.join()


    def terminate(self):
        self._pool.terminate()

