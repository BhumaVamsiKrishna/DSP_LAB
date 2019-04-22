# It is a program to find inverse of a matrix using numpy
import numpy as np
print('Enter the square matrix of any order ;') 
print('Enter the matrix in the form [[a11,a12,a.....a1n],........,[ai1,....,ajn]]')
a=input()
d=np.linalg.det(a)
print('Determinant = %f',d)
if(d==0):
	print('Determinant cannot be found since Determinant=0')
else: 
	i=np.linalg.inv(a)
	print('Determinant of given matrix is ;')
	print i
p=np.linalg.pinv(a)
print('Psuedo Inverse of given marix is ;')
print p

