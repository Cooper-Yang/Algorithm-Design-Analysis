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

	if len(argv[1]) == 1 or len(argv[2]) == 1:
		return int(argv[1])*int(argv[2])

	# input will be some power of ten
	# get the lower even number when the result is odd number
	power = min(len(argv[1]), len(argv[2]))/2*2

	# 12345 should be divided as 123 and 45, not 12 and 345
	a = argv[1][:-(power/2)]
	b = argv[1][-(power/2):]
	c = argv[2][:-(power/2)]
	d = argv[2][-(power/2):]

	if len(a) == 1 or len(c) == 1:
		ac = int(a)*int(c)
	else:
		ac = karatsuba([0, a, c])
	if len(b) == 1 or len(d) == 1:
		bd = int(b)*int(d)
	else:
		bd = karatsuba([0, b, d])
	if int(a)+int(b) < 20 or int(c)+int(d) < 20:
		a_b_c_d = (int(a)+int(b))*(int(c)+int(d))
	else:
		a_b_c_d = karatsuba([0, str(int(a)+int(b)), str(int(c)+int(d))])

	result = (10**power)*ac + (10**(power/2))*(a_b_c_d-ac-bd) + bd

	return result

if __name__ == "__main__":
	if len(sys.argv) is not 3 or len(sys.argv[1]) != len(sys.argv[2]):
		print 'illegal input'
	else:
		print 'the product of '+sys.argv[1]+' and '+sys.argv[2]+' is: '+str(karatsuba(sys.argv))
