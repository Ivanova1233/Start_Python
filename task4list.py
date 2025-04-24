List список
[1,1.2,'привет']
a = [] # Пустой список
b = list() # Пустой список
a = [1,1.1,'a']
print(a) # [1,1.1,'a']
a = [1,1.1,'a']
a[0] ='a'
a[1]= 'б'
a[-1] = 'в'
a = [1,2,3]
a = [1,1.1,'a']
del a[0]
del a[1]
del a[-1]
del a
a = [1,2,3]
b = [4,5,6]
c = a+b
print(c)
a += b
help(list)
a = [1,1,3,1]
a.count(1)
a = [1,2,3]
a.copy()
a = [1,2,3]
a.reverse()
a = [2,1,3]
a.sort()
a = [2,1,3]
a.sort(reverse=True)
from copy import deepcopy
a = [1,2,[1,2,3]]
b = deepcopy(a)
b[2][0] = 10
print(a)