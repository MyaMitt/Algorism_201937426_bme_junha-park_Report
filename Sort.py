import numpy as np
from heap import Heap


def SelectionSort(raw_array, n):
    array = np.copy(raw_array)
    
    for i in range(n-1):
        tmp, idx = __Max(array, n-i)

        print(array[:idx], array[idx], array[idx+1:n-i],array[n-i:])

        array[idx] = array[n-i-1]
        array[n-i-1] = tmp


    return array

def BubbleSort(raw_array, n):
    array = np.copy(raw_array)

    for i in range(1, n):
        checkSort = True
        for j in range(n-i):
            if(array[j] > array[j+1]): 
                array[j], array[j+1] = array[j+1], array[j]
                checkSort = False
            print(array[:j], array[j:j+2], array[j+2:])
        print('\n')
        if checkSort:
            break
    return array

def InsertSort(raw_array, n):
    array = np.copy(raw_array)
    print(array)

    for i in range(1, n):
        loc = i-1
        tmp = array[i]

        print(array[:i],array[i], array[i+1:])

        while ( loc >= 0 and tmp < array[loc]):
            array[loc + 1] = array[loc]
            loc -= 1

        array[loc+1] = tmp
        print(array[:i+1], array[i+1:],'\n')
        
    return array

def MergeSort(raw_array, p, r):
    array = np.copy(raw_array)
    __MergeSort(array, p, r)
    return array

def __MergeSort(array, p, r):
    print(array[p:r+1])
    if p < r :
        q = (p + r) // 2

        __MergeSort(array, p, q)
        __MergeSort(array, q+1, r)
        __merge(array, p, q, r)
def __merge(array, p, q, r):
    i = p
    j = q + 1
    t = 0


    tmp = np.empty(len(array[p:r+1]), dtype=np.int64)
    while (i <= q and j <= r):
        if(array[i] <= array[j]):
            tmp[t] = array[i]
            t += 1
            i += 1
        else:
            tmp[t] = array[j]
            t += 1
            j += 1
        
    while (i<=q):
        tmp[t] = array[i]
        t += 1
        i += 1
    
    while (j<=r):
        tmp[t] = array[j]
        t += 1
        j += 1
    
    array[p:r+1] = tmp
    print(tmp)

def quickSort(raw_array, p, r):
    array = np.copy(raw_array)
    __quickSort(array, p, r)
    return array

def __quickSort(array, p, r):
    if p < r:
        q = __partition(array, p, r)
        
        __quickSort(array, p, q-1)
        __quickSort(array, q+1, r)
        

def __partition(array, p, r):
    x = array[r]
    print('x:', x)
    print(array[p:r+1])
    i = p-1

    for j in range(p, r):
        if(array[j] <= x):
            i += 1
            array[i], array[j] = array[j], array[i]
    
    array[i+1], array[r] = array[r], array[i+1]

    print(array[p:i+1], x, array[i+2:r+1])

    return i+1
    
def __Max(array, n):
    tmp = array[0]
    idx = 0
    for i in range(1, n):
        if tmp < array[i]:
            tmp = array[i]
            idx = i

    return tmp, idx

def HeapSort(raw_array, n):
    arr = np.copy(raw_array)

    heap = Heap(arr)

    for i in range(n, 0, -1):
        print('i=', i, '_'*10)
        
        heap.printHeap(i+1)
        
        arr[0], arr[i] = arr[i], arr[0]
        heap.printHeap(i)
        print(arr[:i],end='')
        print(arr[i:]) 
        heap.heapify(0, i-1)

    return np.flip(arr)