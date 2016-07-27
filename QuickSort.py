# -*- coding: utf-8 -*-
"""
Quick Sort algorithm

Usage:

	QuickSort.py pivot_mode input_data

		pivot_mode = 1: Use the first element as pivot
		pivot_mode = 2: Use the last element as pivot
		pivot_mode = 3: Use the median of first, last, middle element
		pivot_mode = 4: Use random element as pivot
"""

import sys
import os
from random import randint

def quick_sort(input_array=None, start=None, end=None, pivot_mode=None):
	"""
	:type input_array: list
	:type start: int
	:type end: int
	:type pivot_mode: int
	"""
	swap_times = 0

	if end-start <= 0:
		return 0

	if pivot_mode == 1:
		# use first element as pivot
		pivot = start
	elif pivot_mode == 2:
		# use the last element as pivot
		pivot = end
	elif pivot_mode == 3:
		# use the median of the first, last and middle element
		a = int(input_array[(start+end)/2])-int(input_array[start])
		b = int(input_array[end])-int(input_array[(start+end)/2])
		c = int(input_array[end])-int(input_array[start])
		if (a >= 0 and b >= 0) or (a <= 0 and b <= 0):
			pivot = (start+end)/2
		else:
			if (a <= 0 <= c) or (a >= 0 >= c):
				pivot = start
			else:
				pivot = end
	elif pivot_mode == 4:
		# use random pivot
		pivot = randint(start, end)
	else:
		raise ValueError

	if pivot != start:
		input_array[start], input_array[pivot] = input_array[pivot], input_array[start]
		pivot = start

	i = start+1
	for j in range(i, end+1):
		if int(input_array[j]) < int(input_array[pivot]):
			input_array[i], input_array[j] = input_array[j], input_array[i]
			i += 1
	if pivot != i-1:
		input_array[pivot], input_array[i-1] = input_array[i-1], input_array[pivot]
		pivot = i-1
	swap_times += (end-start)

	swap_times += quick_sort(input_array, start, pivot-1, pivot_mode)
	swap_times += quick_sort(input_array, pivot+1, end, pivot_mode)
	return swap_times

def main_func(input_argv):
	"""
	handle input file
	:type input_argv: list
	"""
	try:
		input_path = os.path.abspath(input_argv[2])
		mode = int(input_argv[1])
		if not 1 <= mode <= 4:
			raise ValueError
	except ValueError:
		sys.exit(1)
	input_file = open(input_path, 'r')
	input_array = input_file.read().split()
	total_swap = quick_sort(input_array, 0, len(input_array)-1, mode)
	print total_swap
	# print input_array

if __name__ == "__main__":
	main_func(sys.argv)