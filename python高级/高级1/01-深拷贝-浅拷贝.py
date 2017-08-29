a = [11, 22, 33]
#浅拷贝
b = a

#深拷贝
import copy
c = copy.deepcopy(a)

print(id(a))
print(id(b))
print(id(c))


a = [11, 22, 33]
b = [44, 55, 66]

c = [a, b]

d = c

e = copy.deepcopy(c)
f = copy.copy(c)

a.append(00)
print(c[0])
print(e[0])
print(f[0])
