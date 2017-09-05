from multiprocessing import Queue

q = Queue(2)
print(q.qsize())

q.put('aaa')
print(q.qsize())
print(q.get())
print(q.qsize())
print(q.empty())#如果队列为空，返回True

# 进程池间通信
from multiprocessing import Manager,Pool

q = Manager().Queue()
po = Pool()
