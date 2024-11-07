import numpy as np

#random integer
randomnumber = np.random.randint(20)
#random float
randomfloat = np.random.rand()

#random array 1d

randomarray= np.random.randint(10, size =(5))

#random 2D array

random2darray = np.random.randint(10, size = (3,4))

#choice 

x = np.random.choice([3, 5, 7, 9])

#Generate a 2-D array with 3 rows, each row containing 5 random numbers:
y = np.random.rand(3,5)

z = np.random.rand(5)
print(randomnumber)
print(randomfloat)

print(randomarray)

print(random2darray)

print(x)

print(y)

print(z)