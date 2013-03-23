#!/usr/bin/python
def partition(inlist, low, high):
	pivot=inlist[low]
	while(low<high):
		while(low<high) and inlist[high]>=pivot:
			high -= 1
		inlist[low]=inlist[high]
		while(low<high) and inlist[low]<=pivot:
			low += 1
		inlist[high]=inlist[low]
	inlist[low]=pivot
	return low

def quick_sort(inlist, low, high):
	if low<high:
		indx = partition(inlist, low, high)
		quick_sort(inlist, low, indx-1)
		quick_sort(inlist, indx+1, high)

def QSort(inlist):
	high = len(inlist)-1
	quick_sort(inlist, 0, high)
	return inlist

if __name__=="__main__":
	t = [3, 2, 3, 4, 7, 1, 5, 6, 6]
	print QSort(t)
