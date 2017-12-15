import numpy as np

ndarray=np.array([33,77,55])
#print type of array
print(type(ndarray))
#print shape of array
print(ndarray.shape)
#accessing ndarray is similar to list
print(ndarray[0],ndarray[1],ndarray[2])
#ndarrays are mutable
ndarray[0]=333
#first element is changed here
print(ndarray[0],ndarray[1],ndarray[2])
#ndarrays are typed ,i.e only one kind of elements are stored,so the below code gives error
# ndarray[0]="hi" 

#two dimentional array

ta=np.array([[1,2,3,4],[5,6,7,8]])
print(ta)
print(type(ta))
print(ta.shape)
print(ta[0,0],ta[0,1],ta[1,3])

#other ways to create ndarrays

#2x2 array of 0's
print(np.zeros((2,2)))

#2x2 array filled with 9.0
print(np.full((2,2),9.0))

#2x2 array of diagonal 1's and others 0's
print(np.eye(2,2))

#array of 1's
print(np.ones((2,2)))

#array of random size
print(np.random.random((2,3)))