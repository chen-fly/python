def w1(func):
    def inner():
        print('---正在验证权限---')
        func()
    return inner

def f1():
    print('---1---')

def f2():
    print('---2---')

#innerFunc = w1(f2)()
f2 = w1(f2)()
