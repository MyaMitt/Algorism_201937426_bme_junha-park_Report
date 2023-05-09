class Heap: 
    def __init__(self, array):
        assert(len(array) != 0)

        self.__arr = array
        self.__n = len(array)
        self.__buildHeap()

    def __str__(self) -> str:
        result = ''

        checkPoint = 1
        for i, v in enumerate(self.__arr):
            if i == checkPoint:
                checkPoint += 1
                checkPoint *= 2
                checkPoint -= 1

                result += '\n'
            result += str(v)
            result += ' '
        return result

    def printHeap(self, k):
        result = ''

        checkPoint = 1
        for i in range(k):
            v = self.__arr[i]
            if i == checkPoint:
                checkPoint += 1
                checkPoint *= 2
                checkPoint -= 1

                result += '\n'
            result += str(v)
            result += ' '

        print(result)

    def __buildHeap(self):
        for i in range(self.__n, -1, -1):
            self.heapify(i, self.__n)

    def heapify(self, k, n):
        left = 2*k+1
        right = 2*k+2

        if right < n:
            if self.__arr[left] < self.__arr[right]:
                smaller = left
            else:
                smaller = right

        elif (left < n):
            smaller = left
        else:
            return
        
        if self.__arr[smaller] < self.__arr[k]:
            self.__arr[smaller], self.__arr[k] = self.__arr[k], self.__arr[smaller]
            self.heapify(smaller, n)
