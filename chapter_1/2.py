import numpy as np

array_1_2d = np.array([[1, 2], [3, 4]])
array_2_2d = np.array([[5, 6], [7, 8]])
array_3_2d = np.array([[0, 10], [11, 12]])

array_3d = np.array([array_1_2d, array_2_2d, array_3_2d])

print(array_3d)
print(array_3d.shape)
print(array_3d.flatten())
print(array_3d.reshape(2,6))


'''
# Flatten sudoku_game
flattened_game = sudoku_game.flatten()

# Print the shape of flattened_game
print(flattened_game.shape)

# Reshape flattened_game back to a nine by nine array
reshaped_game = flattened_game.reshape(9,9)

# Print sudoku_game and reshaped_game
print(sudoku_game)
print(reshaped_game)
'''