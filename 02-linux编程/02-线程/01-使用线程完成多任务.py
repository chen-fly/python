import time
from threading import Thread

def test():
    print('---昨晚喝多了，下次少喝点---')
    time.sleep(1)

for i in range(5):
    t = Thread(target=test)
    t.start()


#from threading import Thread
#import time
#def test():
#    print('---...---')
#    time.sleep(1)

#for i in range(10):
#    t = Thread(target=test)
#    t.start()



#导入互斥锁
from threading import Lock
#创建一把互斥锁，默认未上锁
mutex = Lock()
#上锁,上锁后，如果有其他地方等待上锁，会导致其他地方阻塞，直至此处解锁
mutex.acquire()
#解锁
mutex.release()
