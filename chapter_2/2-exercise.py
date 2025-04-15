# Create an array which contains row data on the largest tree in tree_census
largest_tree_data = tree_census[tree_census[:, 2] == 51]
print(largest_tree_data)

# Slice largest_tree_data to get only the block ID
largest_tree_block_id = largest_tree_data[:, 1]
print(largest_tree_block_id)

# Create an array which contains row data on all trees with largest_tree_block_id
trees_on_largest_tree_block = tree_census[tree_census[:,1] == 501882]
print(trees_on_largest_tree_block)

# Create an array of row_indices for trees on block 313879
row_indices = tree_census[:, 1] == 313879

# Create an array which only contains data for trees on block 313879
block_313879 = tree_census[:,1][row_indices]
print(block_313879)
'''
# Create an array of row_indices for trees on block 313879
row_indices = np.where(tree_census[:, 1] == 313879)

# Create an array which only contains data for trees on block 313879
block_313879 = tree_census[row_indices]
print(block_313879)'''

#Create and print a 1D array called trunk_stump_diameters, which replaces a tree's trunk diameter with its stump diameter if the trunk diameter is zero.


# Create and print a 1D array of tree and stump diameters
trunk_stump_diameters = np.where(tree_census[:,3] == 0,  tree_census[:,2], tree_census[:,3])
print(trunk_stump_diameters)