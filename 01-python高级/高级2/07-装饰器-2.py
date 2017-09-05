def w1(func):
    def inner():
        print('---正在验证权限---')
        func()
    return inner
@w1
def f1():
    print('---1---')

@w1
def f2():
    print('---2---')

f1()
f1()
