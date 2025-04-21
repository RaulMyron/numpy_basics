# Broadcasting

# shape tem que ser igual da direita p esquerda

#shape(10,5)
#shae(10,1)
#compativel, não o contrario

# Transpose rgb_array
transposed_rgb = np.transpose(rgb_array, axes=(1, 0, 2))
plt.imshow(transposed_rgb)
plt.show()

np.split(rgb, 3, axis=2)
np.stack