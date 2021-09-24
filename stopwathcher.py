import time
from threading import Thread

class Stopwatcher:
    def __init__(self):
        self.t_start = None
        self.t_finish = None
        self.t = None
    def start(self):
        self.reset()
        self.t_start = time.time()
    def finish(self):
        self.t_finish = time.time()
        self.t = self.t_finish - self.t_start
    def reset(self):
        self.t_start = None
        self.t_finish = None
        self.t = None

if __name__ == "__main__":
    t = time.time()
    time.sleep(1)
    print(time.time() - t)