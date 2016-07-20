# -*- coding: utf-8 -*-
"""
Karatsuba Multiplication Algorithm (Recursive)

KaratsubaMultiplication.py 1st_num 2nd_num
"""

import sys

def karatsuba(argv):
	"""
	:type argv: list
	:return:
	"""
	a = argv[1][:len(argv[1]) / 2]
	b = argv[1][len(argv[1]) / 2:]
	c = argv[2][:len(argv[2]) / 2]
	d = argv[2][len(argv[2]) / 2:]

	if len(a) == 1 or len(c) == 1:
		ac = int(a)*int(c)
	else:
		ac = karatsuba([a, c])
	if len(b) == 1 or len(d) == 1:
		bd = int(b)*int(d)
	else:
		bd = karatsuba([b, d])
	if int(a)+int(b) < 20 or int(c)+int(d) < 20:
		a_b_c_d = (int(a)+int(b))*(int(c)+int(d))
	else:
		a_b_c_d = karatsuba([str(int(a)+int(b)), str(int(c)+int(d))])

	power = max(len(argv[1]), len(argv[2]))

	result = (10**power)*ac + (10**(power/2))*(a_b_c_d-ac-bd) + bd

	return result

if __name__ == "__main__":
	if len(sys.argv) is not 3 or len(sys.argv[1]) != len(sys.argv[2]):
		print 'illegal input'
	karatsuba(sys.argv)
