import Sort
import numpy as np

arr = np.random.randint(low=0, high=100, size=20)


print('\n\narray: ',arr)

key = input('\nselect method by enter number\n\n1.SelectionSort\n2.BubbleSort\n3.insertSort\n4.MergeSort\n5.quickSort\n6.HeapSort\n\nselect:')

if key == '1':
    print('SelectionSort'+'_'*20)
    print(Sort.SelectionSort(arr, len(arr)), end='\n\n')
elif key == '2':
    print('BubbleSort___'+'_'*20)
    print(Sort.BubbleSort(arr, len(arr)))
elif key == '3':
    print('\ninsertSort___'+'_'*20)
    print(Sort.InsertSort(arr, len(arr)))
elif key == '4':
    print('MergeSort___'+'_'*20)
    print(Sort.MergeSort(arr, 0, len(arr)-1))
elif key == '5':
    print('quickSort___'+'_'*20)
    print(Sort.quickSort(arr, 0, len(arr)-1))
elif key == '6':
    print('heapSort___'+'_'*20)
    print(Sort.HeapSort(arr, len(arr)-1))
else:
    print('wrong input')