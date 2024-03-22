
r=np.genfromtxt('Linalgr.txt')
print('Исходный массив r')
print(r)

x = np.dot(B,p)
print ('x =', x)

y = np.dot(A,x)
print ('y =', y)

z = p+r+q
print ('z =', z)
s = np.dot(z,r)
print ('s =', s)


A
1 2 3
1 2 1
3 2 0

B
4 1 2
0 4 3
1 1 1

p
0.1 1.7 -1.5

q
-1.6 0.8 1.1
