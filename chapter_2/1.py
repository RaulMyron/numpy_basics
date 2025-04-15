import numpy as np

array = np.array([2, 4, 6, 8, 10])

print(array[0])

array_2d = np.array(
    [[2, 4, 6, 8, 10], [10, 8, 4, 2, 6], [2, 4, 6, 8, 10], [2, 4, 6, 8, 10]]
)

print(array_2d)

print(array_2d[:, 3])  # acess cols

print(array_2d[1:3, 1:2])  # slice 2d, row start stop col stop start
print(array_2d[1:4, 1:4])  # slice 2d, row start stop col stop start
print(array_2d[1:4:2, 1:4:2])  # slice 2d, row start stop col stop start

print(np.sort(array_2d))
print(np.sort(array_2d, axis=0))
