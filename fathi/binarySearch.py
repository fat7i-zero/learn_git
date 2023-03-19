from heapSort import heapSort
from random import randint


def binarySearch(arr, i, j, item):
    mid = (j+i)//2

    if arr[mid] == item:
        return True
    elif (i < j):
        if (arr[mid] > item):
            return binarySearch(arr, i, mid - 1, item)
        else:
            return binarySearch(arr, mid + 1, j, item)
    else:
        return False


arr = []
for i in range(10):
    arr.append(randint(0, 20))
heapSort(arr)
print(arr)
print("-"*50)
n = len(arr)
x = binarySearch(arr, 0, n-1, 15)

if x:
    print("Found")
else:
    print("Not found")
