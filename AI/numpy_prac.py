import numpy as np

a = np.array([[12,32,43], [32,435,54]], dtype = 'int16')
print(a)

b = np.array([4.0, 32.0, 31.0])
print(b)

#Get Dimension
print(a.ndim)
print(b.ndim)

#Get Shape
print(a.shape)
print(b.shape)

#Type
print(a.dtype)
print(b.dtype)

#itemsize
print(a.itemsize)
print(b.itemsize)

#Total size
print(a.nbytes)
print(b.nbytes) #or b.size * b.itemsize

#Get a specific element [r, c]
print(a[1, 2])

#Get a specific row [r, :]
print(a[1, :])

#startindex:endindex:steps
print(a[0, 0:2:1])

#an array of same number
c = np.full((4,2,2), 55)
print(c)

#copying an array size with a fixed value
d = np.full_like(a, 32)
print(d)

#matrix of random decimal numbers (r, c)
e = np.random.rand(3,2)
print(e)

#matrix of random integers numbers (starting_number, ending number, size)
f = np.random.randint(-1,7, size= (3,4))
print(f)

#idntity matrix
g = np.identity(5)
print(g)

h = np.array([[1,2,3]])
h = np.repeat(h, 3, axis=0) 
print(h)

i = np.full((5,5), 1)   // np.ones((5,5))
i[1, 1:-1] = 0
i[3, 1:-1] = 0
i[2, :] = [1, 0, 9, 0, 1]
print(i)


j = np.ones((5,5))
k = np.zeros((3,3))
k[1,1] = 9
j[1:-1, 1:-1] = k
print(j)


#copying arrays
l = a.copy()
l[1, 1] = 99
print(l)





