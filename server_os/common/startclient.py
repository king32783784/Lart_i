import multiprocessing
import time
clients=('a','b','c')
isolists=('iso1','iso2','iso3',)
class ClockProcess(multiprocessing.Process):
    def __init__(self, interval):
        multiprocessing.Process.__init__(self)
        self.interval = interval

    def run(self):
        n = 5
        while n > 0:
            print("the time is {0}".format(time.ctime()))
            time.sleep(self.interval)
            n -= 1
if __name__ == '__main__':
    plist = []
    clientnum = len(clients)
    isonum = len(isolists)
    if clientnum >=1 and isonum >=1:
        for isotest in isolists:
            if clientnum >=1:
                p = ClockProcess(3)
                plist.append(p)
                p.start()
                clientnum -= 1
        for p in plist:
            p.join()

