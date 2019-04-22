
a=input('Enter the no.of rows for 1st matrix')
b=input('Enter the no.of columns for 1st matrix')
c=input('Enter the no.of rows for 2nd matrix')
d=input('Enter the no.of columns for 2nd matrix')
e={}
f={}
print('Enter the Elements for matrix1 ')
for i in range (0,a,1):
	for j in range (0,b,1):
		e[i,j]=int(input('Enter the element'))
print('Enter the Elements for matrix2 ')
for i in range (0,c,1):
	for j in range (0,d,1):
		f[i,j]=int(input('Enter the element'))
c={}
for i in range (0,a,1):
	for j in range (0,d,1):
		c[i,j]=0
print('Multplication of two matrices is ; ')
for i in range(0,a,1):
    for j in range(0,d,1):
		for k in range (0,b,1):
			c[i,j]=c[i,j]+(e[i,k]*f[k,j])

print c





