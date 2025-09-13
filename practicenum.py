import numpy as np
print(np.__version__)

a=[1,2,3,4,5]
b=np.array(a,dtype=float)
c=np.array(a,dtype=int)
print(b)
print(c)
for i in b:
    print(i)


for i in np.nditer(c):
    print(i)


print(c[1])
print(c[3])
print(b[1])

d=np.array([[1,2,3],[1,2,3]])
print(d)
print(d[0][1])

e=np.array([[[1,2],[11,22]],[[111,112],[221,222]]],order="F")
print(e.ndim)
print(e[0][1][1])
for i in np.nditer(e):
    print(i)

a=[1,2,3,4]
v=np.fromiter(a,dtype=int,count=2)
print(v)