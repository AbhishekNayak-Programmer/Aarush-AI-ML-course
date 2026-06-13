import numpy as np

arr = np.array([1,2,3,5,8])

arr = np.array([
    [1,2,3],
    [4,5,6]
])

print(arr)
print(arr.shape)
print(arr.ndim)
print(arr.size)
print(arr.dtype)

zeroMat = np.zeros((10,15))
# print(zeroMat)

oneMat = np.ones((10,15))
# print(oneMat)

customNumMat = np.full((2,3), 99)
print(customNumMat)

arr = np.arange(1, 101)
print(arr)

# arr = np.linspace(0, 10, 5)
# print(arr)

arr = np.arange(1, 13)
new_arr = arr.reshape(3,4)

print(new_arr)

arr = np.array([1,2,3,4])
print(arr[1])

arr = np.array([[1,2],[3,4]])
print(arr[1][0])

arr = np.array([1,2,3,4])
print(arr[1:3])


arr1 = np.array([1,2,3,4])
arr2 = np.array([5,6,7,8])

print(arr1 + arr2)
print(arr1 - arr2)
print(arr1 * arr2)
print(arr1 / arr2)

arr = np.array([1,2,3,4])
print(arr + 10)
print(np.sqrt(arr))

print(arr.sum())
print(arr.max())
print(arr.min())
print(arr.mean())

arr = np.array([1,2,3,4])
print(arr[arr >= 3])

arr = np.array([True, False, True])
print(arr[arr == True])

arr = np.array([35,456,2,25])
print(np.sort(arr))

arr1 = np.array([1,2,3,4])
arr2 = np.array([5,6,7,8])

print(np.concatenate((arr1, arr2)))