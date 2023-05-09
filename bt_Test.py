import BinaryTree
import numpy as np
BT = BinaryTree.BinaryTree()

#BT.append(2)
#BT.append(4)
#BT.append(5)
#BT.append(3)


#BT.append(1)

#arr = (np.random.choice(100, 20, replace=False))

arr = [73, 70, 11, 94, 71, 44,  9, 26, 58, 43, 98, 54, 48, 79,  4, 38, 55, 88,  0, 46]

print(arr)

#BT.append_to_list(arr)

for i, key in enumerate(arr):
    print('='*100)
    print(f'number: {i+1}\t insert key : {key}')
    print('-'*100)

    BT.append(key)
    BT.show_tree()


print('='*100)
print(f'number: {i+1}\t delete key : {44}')
print('-'*100)

BT.delete_node(44)
BT.show_tree()