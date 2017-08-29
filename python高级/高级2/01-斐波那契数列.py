def creatNum():
    a,b = 0,1
    print('---start---')
    for i in range(10):
        print("---1---")
        #增加了yield的函数相当于一个生成器
        yield b
        print('---2---')
        a,b = b,a+b
        print('---3---')
    print('---stop---')
creatNum()#直接调用函数，并不会有结果

a = creatNum()
#next(a)#执行到yield语句停止
#next(a)#从yield开始执行，停止到第二次循环yield处，以此类推

#for temp in a:
#    print(temp)

ret = a.__next__()
print(ret)

#注意
#next(a)
#a.__next__()
#以上两种方式是一样的
