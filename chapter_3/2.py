import numpy as np

# Vectorized operations

# Define a scalar function
def my_function(x):
    return x**2 + 3 * x + 5


# Create a NumPy array
arr = np.array([1, 2, 3, 4])

# Vectorize the function
vectorized_func = np.vectorize(my_function)

# Apply the vectorized function to the array
result = vectorized_func(arr)

print(result)  # Output: [ 9 17 29 45 ]
