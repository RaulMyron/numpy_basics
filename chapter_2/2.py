import numpy as np

# Filtering arrays

# Creating masks booolean indexing
one_to_five = np.arange(1, 6)
mask = one_to_five % 2 == 0
print(mask)
print(one_to_five[mask])  # can pass a mask as a id

# class_ids[:,0][class_ids[:,1]%2==0] #mask that from the get the ids from the fist col, if the values in the rest of division by 2 is 0 on the socnd col it exists

# Np.where

# Cria condições e cria o array com base na condição

# np.where(lass_ids[:,1]%2==0)
# retorna uma lista de ids

# row, col = np.where(sudoku_game == 0)

# ou np.where(sudoku_game == 0, "", sudoku_game)
# substitiu os elementos '' para 0, e mantem o sudoku_game

