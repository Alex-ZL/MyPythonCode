#usr/bin/env python
##Find the greatest sum of all sub-arrays, and the sub-array

def find_greatest_sum(inlist):
	if len(inlist) == 0:
		print "it's empty lis"
		exit(0)
	
	cur_sum = 0
	greatest_sum = 0
	start_pos = 0
	end_pos = 0 
	for pos in xrange(len(inlist)):
		cur_sum += inlist[pos]

		if cur_sum < 0:
			cur_sum = 0
			start_pos = pos+1

		if cur_sum > greatest_sum:
			greatest_sum = cur_sum
			end_pos = pos+1

	if greatest_sum == 0:
		greatest_sum = inlist[0]
		start_pos = 0
		end_pos = 1
		for pos in xrange(len(inlist)):
			if inlist[pos] > greatest_sum:
				greatest_sum = inlist[pos]
				start_pos = pos
				end_pos = pos+1
	
	return greatest_sum, inlist[start_pos:end_pos]

tlist = [2,4,-1,-8,3,5,-2,1,9,-10,6,-2,3,4,5,-1,12]
print find_greatest_sum(tlist)
slist = [-3,-2,-3,-4]
print find_greatest_sum(slist)
