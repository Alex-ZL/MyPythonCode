def patition(inlist, low, high):
	povit = inlist[low]
	while low < high:
		while (low < high and povit <= inlist[high]):
			high -= 1
		inlist[low] = inlist[high]
		while (low < high and povit > inlist[low]):
			low += 1
		inlist[high] = inlist[low]
	inlist[low] = povit
	return low

def q_sort(inlist, low, high):
	if low < high:
		indx = patition(inlist, low, high)
		q_sort(inlist, low, indx-1)
		q_sort(inlist, indx+1, high)


if __name__ == "__main__":
	t = [2, 3, 4, 5, 12, 45, 3, 1]
	q_sort(t, 0, 7)
	print t
