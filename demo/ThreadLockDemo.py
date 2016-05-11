import threading
import time
mutex = threading.Lock()
class DBSaverThread(threading.Thread):
    def run(self):
        while(True):
            mutex.acquire()
            time.sleep(100)
            print("------------------------存储线程执行---------------------------------")
            mutex.release()
