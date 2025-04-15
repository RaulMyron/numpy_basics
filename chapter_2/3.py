import numpy as np

# Adding and removing data

# Concatenate

class_id_size = np.array([[1, 22], [2, 21], [3, 27], [4, 26]])
new_class = np.array([[5, 30], [5, 17]])

print(np.concatenate((class_id_size, new_class)))

grade = np.array([[1, "jamees"], [1, "george"], [3, "amy"], [3, "meehir"]])

print(np.concatenate((class_id_size, grade), axis=1))
nueva_classe = np.concatenate((class_id_size, grade), axis=1)

array_id = np.array([1, 2, 3])
column_2d = array_id.reshape((3, 1))  # 3 colunas, 1 linha adiciona mais uma axis
print(column_2d)


print(np.delete(nueva_classe, 1, axis=0)) # deleta elemento 2 especificada, de maneira a liinha
print(np.delete(nueva_classe, 1, axis=1)) # deleta elemento 2 especificada, de maneira a coluna
print(np.delete(nueva_classe, 1)) #flattens it all, só deleta todos os indices 