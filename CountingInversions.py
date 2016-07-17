# -*- coding: utf-8 -*-
"""
Counting Inversions Algorithm
"""

import sys
import os

def counting_inversions(input_array):
	"""
	counting inversions using merge sort algorithm in nlog(n) time
	:type argv: list
	"""
	number_of_inversions = 0
	if len(input_array) <= 1:
		return number_of_inversions
	left_array = input_array[0:len(input_array)/2]
	right_array = input_array[len(input_array)/2:len(input_array)]
	number_of_inversions += counting_inversions(left_array)
	number_of_inversions += counting_inversions(right_array)
	j = 0
	k = 0
	try:
		for _ in range(0, len(input_array)):
			if left_array[j] < right_array[k]:
				j += 1
			if left_array[j] > right_array[k]:
				k += 1
				number_of_inversions += (len(left_array) - j)
	except IndexError:
		pass
	return number_of_inversions

def main_func(input_argv):
	"""
	handle input file
	:type argv:
	"""
	try:
		input_path = os.path.abspath(input_argv[1])
	except ValueError:
		sys.exit(1)
	input_file = open(input_path, 'r')
	input_array = input_file.read().split()
	total_inversions = counting_inversions(input_array)
	print total_inversions

if __name__ == "__main__":
	main_func(sys.argv)
