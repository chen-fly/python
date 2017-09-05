from multiprocessing import Pool
import time
import random
import os

def worker():
    for i in range(random.randint(1,3)):
        print('---pid = %d---'%os.getpid())

pool = Pool(3)

#阻塞方式
for i  in range(10):
    pool.apply(worker)
