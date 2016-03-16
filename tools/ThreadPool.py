#-*-coding:utf8-*-
import threading
import time

class ThreadPool(object):
    def __init__(self,size):

        threading.Thread.__init__(self)
        self._size = size
        self._threads = []
        self._tasks = []

        """http://www.cnblogs.com/nsnow/archive/2010/04/07/1706794.html"""
        self._listLock = threading.Condition(threading.Lock())
        self._taskLock = threading.Condition(threading.Lock())

        self._resizeLock = threading.Condition(threading.Lock())
        self._isClose = False #关闭的线程池不允许修改

    def append(self, thread):
        if(self._tasks < self._size):
            self._taskLock.acquire()
            try:
                self._tasks.append(thread)
            finally:
                self._taskLock.release()


t = ThreadPool(20)
t.__size = 50
print(t.__size)

