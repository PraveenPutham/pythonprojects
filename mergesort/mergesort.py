

def mergeSort(arr):
	if (len(arr) > 1):
		mid = int(len(arr)/2)
		leftArr = arr[:mid]
		rightArr = arr[mid:]
		mergeSort(leftArr)
		mergeSort(rightArr)

		i = j = k = 0
		while ( i < len(leftArr) and j < len(rightArr)):
			if leftArr[i] < rightArr[j]:
				arr[k] = leftArr[i]
				i = i +1
			else:
				arr[k] = rightArr[j]
				j = j + 1
			k = k + 1

		# to check for the remaining elements in Left and Right Array
		while (i <len(leftArr)):
			arr[k]=leftArr[i]
			i = i + 1
			k = k + 1

		while (j < len(rightArr)):
			arr[k] = rightArr[j]
			j = j + 1
			k = k + 1
		#print("Modified = {0}".format(printArray(arr)))


def printArray(arr):
	myString = ''
	for i in range(len(arr)):
		myString  += str(arr[i]) + ' '
	return myString


if __name__ == '__main__':
	arr = [23,34,1,43,24,6]
	print("Initial Array = {0}".format(printArray(arr)))
	#print('calling merge')
	mergeSort(arr)
	print("Sorted Array = {0}".format(printArray(arr)))


