#usr/bin/evn python
## quick sort implamented in python, just for exercise
def partition(inlist, low, high):
	pivotkey = inlist[low]

	while(low < high):
		while(low < high and pivotkey <= inlist[high]):
			high -= 1
		inlist[low] = inlist[high]
		while(low < high and pivotkey >= inlist[low]):
			low += 1
		inlist[high] = inlist[low]
	
	inlist[low] = pivotkey
	
	return low

def quick_sort(inlist, low, high):
	if low < high:
		pivotloc = partition(inlist, low, high)
		quick_sort(inlist, low, pivotloc-1)
		quick_sort(inlist, pivotloc+1, high)

if __name__ == '__main__':
	tlist = [5,1,3,2,4,9,8,7,6]
	quick_sort(tlist,0,8)
	print tlist
