#/usr/bin/python
## A function to group list

allNames=["Alex","Ada","Amy","Debbie","Kobe","Hejus","Jack","Grant",
		"Mike","Evan","Stone","Ben","Johnson","Selena","Lake","Michael"
		]

def random_group(input_list, groupNum=2, seed=5):
	"""gourp the input_list randomly into certain number of groups, seed 
	is for reconstructure the suquence of the input list before the group
	begin"""

	length = len(input_list) 

	#init out_list structure
	out_list = []
	for i in range(groupNum):
		out_list.append([])

	#reconstructure the sequence by seed.
	for x in xrange(length):
		if x*seed < length:
			input_list.append(input_list.pop(x*seed))
		else:
			break
	
	#group input list into several groups.
	for y in xrange(length):
		out_list[y%groupNum].append(input_list[y])

	return out_list


if __name__ == '__main__':
	print random_group(allNames,6)

