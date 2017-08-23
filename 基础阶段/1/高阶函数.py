

import time

def performance(unit):
    def per_dec(f):
        def wrap(*args, **kw):
            t1 = time.time()
            r = f(*args, **kw)
            t2 = time.time()
            if unit == 's':
                t = t2 - t1
            else :
                t = 1000 * (t2 - t1)
            print 'call %s() in %f %s'%(f.__name__, t, unit)
            print r
            return r 
        return wrap
    return per_dec

@performance('ms')
def factorial(n):
    return reduce(lambda x,y: x*y, range(1, n+1))

print factorial(10)