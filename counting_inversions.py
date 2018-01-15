#!/usr/bin/env python 

import sys

inputarray = [line.rstrip('\n') for line in open(sys.argv[1])] #making a list out of the input file

for i in range(0, len(inputarray)):       	#this for loop grabs the list and makes 
	inputarray[i] = int(inputarray[i])		#every item an integer
inputarray = inputarray[1:]

def sort_and_count_inversions(A): 
	if len(A) == 1:
		return A, 0
	else:
		middle = len(A) // 2
		l, lc = sort_and_count_inversions(A[:middle])
		r, rc = sort_and_count_inversions(A[middle:])
		a, sc = sort_and_count_split_inversions(l, r)
		return a, lc + rc + sc

def sort_and_count_split_inversions(l, r):
	resultarray = []
	inversions = 0
	while len(l) and len(r): 
		if l[0] <= r[0]: 
			resultarray.append(l[0])
			l.remove(l[0])
		else:
			resultarray.append(r[0])
			r.remove(r[0])
			numinversions = len(l)
			inversions += numinversions
	if len(l) == 0:
		resultarray += r
	else:
		resultarray += l
	return resultarray, inversions

endresult = sort_and_count_inversions(inputarray)
print endresult[1]