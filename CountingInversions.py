# -*- coding: utf-8 -*-
"""
Counting Inversions Algorithm
"""

import sys
import os

def counting_inversions(input_array):
	"""
	counting inversions using merge sort algorithm in nlog(n) time
	:type input_array: list
	"""
	number_of_inversions = 0
	if len(input_array) <= 1:
		return number_of_inversions
	left_array = input_array[:len(input_array)/2]
	right_array = input_array[len(input_array)/2:]
	number_of_inversions += counting_inversions(left_array)
	number_of_inversions += counting_inversions(right_array)
	temp_i = 0
	j = 0
	k = 0
	try:
		for i in range(0, len(input_array)):
			# element in the left side array should be pop up first while it equal to the right side
			if int(left_array[j]) <= int(right_array[k]):
				input_array[i] = left_array[j]
				j += 1
				temp_i = i+1
				continue
			if int(left_array[j]) > int(right_array[k]):
				input_array[i] = right_array[k]
				number_of_inversions += (len(left_array) - j)
				k += 1
				temp_i = i+1
				continue
	except IndexError:
		if j >= len(left_array):
			for i in range(temp_i, len(input_array)):
				input_array[i] = right_array[k]
				k += 1
		else:
			# k >= len(right_array)
			for i in range(temp_i, len(input_array)):
				input_array[i] = left_array[j]
				j += 1
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
