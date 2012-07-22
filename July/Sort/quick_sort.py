#usr/bin/evn python
## quick sort implamented in python, just for exercise
def partition(inlist, low, high):
	i = low
	j = high
	key = inlist[low]
	flag = True
	while(i!=j):
		if flag:
			if inlist[j] < key:
				inlist[i], inlist[j] = inlist[j], inlist[i]
				flag = False
			j-=1
		else:
			if inlist[i] > key:
				inlist[i], inlist[j] = inlist[j], inlist[i]
				flag = True
			i+=1
	return i

def quick_sort(inlist, low, high):
	if low < high:
		pivotloc = partition(inlist, low, high)
		quick_sort(inlist, low, pivotloc-1)
		quick_sort(inlist, pivotloc+1, high)

tlist = [5,1,3,2,4,9,8,7,6]
print partition(tlist,0,8)
quick_sort(tlist,0,8)
print tlist
