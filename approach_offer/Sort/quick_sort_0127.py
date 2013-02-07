def partition(sort_list, low, high):
	povit = sort_list[low]
	while low < high:
		while (low < high and sort_list[high] >= povit):
			high -= 1
		sort_list[low] = sort_list[high]
		while (low < high and sort_list[low] <= povit):
			low += 1
		sort_list[high] = sort_list[low]
	sort_list[low] = povit
	return low

def q_sort(sort_list, low, high):
	if low < high:
		indx = partition(sort_list, low, high)
		q_sort(sort_list, low, indx-1)
		q_sort(sort_list, indx+1, high)

if __name__ == "__main__":
	t = [6, 5, 4, 3, 2, 2, 2, 1]
	q_sort(t, 0, 7)
	print t
