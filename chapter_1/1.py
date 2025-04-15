import numpy as np

# Create 1d list

python_array = np.random.randint(0, 100, size=10)
print(python_array)

# Convert to np

array = np.array(python_array)
print(array, type(array))

# Creating 2d list

print("-" * 10)

python_array_2d = np.random.randint(0, 100, size=(3, 3))
print(python_array_2d)

np_array_2d = np.array(python_array_2d)
print(np_array_2d, type(np_array_2d))

"""numpy array gotta be the same datatype such as c++, it meanings that
it is faster, no meaning for it to reverify the values inside of the
arr
"""

print("-" * 10)
print(np.zeros((3, 3)))  # tuples (3x3)
print(np.random.random((1, 10)))
print(np.arange(-3, 4)) #good for plot

from matplotlib import pyplot as plt

plt.scatter(np.arange(0, 7), np.arange(-3, 4)) #grafico de ponto
plt.show()
