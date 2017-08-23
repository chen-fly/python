try:
    print(num)
    open('xxx.txt')
    print('...1...')
# except 可能出现异常的名字:
except NameError:
    print('如果捕获到异常后的处理.....')

except FileNotFoundError:
    print('文件不存在')
# python2 使用方式
except NameError,FileNotFoundError:
    print('出现异常了')
# python3 使用方式
except (NameError,FileNotFoundError):

except Exception:
    print('如果用了Exception，那么意味着只要上面的except没有捕获到异常，这个except一定会捕获到')
# 查看异常的名字
except Exception as ret:
    print(ret)
else:
    print('没有异常执行的操作')
finally:
    print('不管有没有异常，最后执行的操作')

print('....2.....')
