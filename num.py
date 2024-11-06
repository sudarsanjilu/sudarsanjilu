import numpy as np
'''arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(type(arr))
print(np.__version__)
print(arr[0])
print(arr[3])
print(arr[0] + arr[3])'''

'''2D array
print("2d Array")
print()
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print(arr2)'''

arr2 = np.eye(10)
print(arr2)

arr3 =np.random.randint(50,100, size=10)
arr4= np.random.randint(100,150, size =5)
arr5 = np.sum(arr3)
arr6= np.mean(arr3)
#arr7= np.maximum(arr3)
arr8= np.median(arr3)
print(arr3)
print(arr4)
print(arr5)
print(arr6)
#print(arr7)
print(arr8)

arr9 = np.random.randint(50,100, size=(8,6))
print(arr9)

#axis =o row and axis =1 means column wise
arr10=arr9.mean(axis=0)
print(arr10)


