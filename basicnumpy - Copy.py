import numpy 
print(numpy.__version__)

import numpy as np
#creating arrays
arr=np.array([]) #emp array
print(arr)




#Dimensuons in array 

#0 dim--with single element
arr1=np.array([7]) 
print(arr1)

#1dim
arr3=np.array([11,12,13]) 
print(arr3)
print(arr3[1])

#2 dim  collection of one dims is 2 dimens
arr11=np.array([[1,2,3],[22,33,44],[11,222,33]]) 
print(arr11)
print(arr11.ndim)

#ndim used to know thw dimensions
print(arr11[0][1]) #no of subscripts [] will increas with no of dimensios
print(arr11[1,2])


#3dim collection of 2 dims is 3 dimens
arr11=np.array([[[1,2],[22,33],[222,333],[111,222]]]) 
print(arr11)
print(arr11.ndim)


print(arr11[0][1][1])
print(arr11[0,1,1])




#asarray with nditer
#creating array with   asarray()
a=[1,2,3,4,5] #a list
b=np.asarray(a)
c=np.asarray(a,dtype=str) #we cangive any data type  for the array by usind dtype
d=np.asarray(a,dtype=float)
print(b)
print(c)
print(d)


#row major order and column major order
#uses where there is 2 dim array
a=[[1,2,3],[11,22,33]]
b=np.asarray(a,order="C")  #row major order means ekements dispplay in row wise
print(b)


#nditer is used when declaring arrats with np.asarray()

for i in np.nditer(b):
    print(i)



#colum wise order

a=[[1,2,3],[11,22,33]]
b=np.asarray(a,order="F")  #colu major order means ekements dispplay in comnl wise
print(b)

for i in np.nditer(b):
    print(i)




#fromiter
a=[1,2,3,4,5,6,7]
b=np.fromiter(a,dtype=int,count=5)
print(b)