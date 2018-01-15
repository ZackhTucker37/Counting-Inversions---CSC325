#!/usr/bin/env python

inputArray = [line.rstrip('\n') for line in open("data.txt")]

for i in range(0, len(inputArray)):
    inputArray[i] = int(inputArray[i])

print inputArray

def merge_sort_with_inversion_count(dataList):
    sortedData = []
    
    if len(dataList) > 1:
        middle = len(dataList) / 2
        left = dataList[:middle]
        right = dataList[middle:]
        merge_sort_with_inversion_count(left)
        merge_sort_with_inversion_count(right)

        i, j, k = 0
        if left[i] <= right[j]:
            sortedData[k] = left[i]
            i += i
        else:
            sortedData[k] = right[j]
            j += j
        k += k
    return sortedData
    
outputArray = merge_sort_with_inversion_count(inputArray)
print(outputArray)