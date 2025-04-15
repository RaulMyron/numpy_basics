import numpy as np
import matplotlib.pyplot as plt

# Create an array of integers from one to ten
one_to_ten = np.arange(1,11)
print(one_to_ten)

# Create a random array of 10 integers and double their values
random_integers = np.random.randint(1, 101, size=10)
doubling_array = random_integers * 2

# Create your scatterplot
plt.scatter(one_to_ten, doubling_array)
plt.show()