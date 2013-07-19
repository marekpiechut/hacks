#!/usr/bin/env python3
import array,unittest,itertools
from math import *

def to_digits(number):
	#How many digits we have
	amount = int(ceil(log(number + 1, 10)))
	digits = array.array('b')
	
	for pos in range(0, amount):
		base = pow(10, pos) 
		digit = int(number / base % 10)
		digits.append(digit)

	return digits

def to_number(digits):
	number = 0
	for pos in range(0, len(digits)):
		base = pow(10, pos)
		number += digits[pos] * base

	return int(number)

def next_from_same_digits(number):
	pass

def brute_force(number):
	digits = to_digits(number)
	permutations = itertools.permutations(digits.tolist())
	
	numbers = set()
	for permutation in permutations:
		permutation_number = to_number(permutation)
		numbers.add(permutation_number)

	print("permutations: {}".format(len(numbers)))
	numbers = list(numbers)
	numbers.sort()
	index = numbers.index(number)
	if index >= len(numbers):
		return numbers[index]
	else:
		return numbers[index + 1]
		
	

class Test(unittest.TestCase):
	def test_to_digits(self):
		digits = {11:[1,1], 4:[4], 1234:[1,2,3,4], 865320865:[8,6,5,3,2,0,8,6,5]}
		for k,v in digits.items():
			#reverse because we're indexing by digi position and not naturally
			v.reverse()
			self.assertEqual(to_digits(k).tolist(), v)

	def test_next_from_same_digits(self):
		numbers = [12, 123, 3244, 234, 3527563, 2234325]
		for number in numbers:
			expected = brute_force(number)
			print("{} < {}".format(number, expected))
			actual = next_from_same_digits(number)
			#self.assertEqual(actual, expected)

	def test_brute_force(self):
		numbers = {12: 21, 342: 423, 1243: 1324}
		for number, expected in numbers.items():
			actual = brute_force(number)
			self.assertEqual(actual, expected)

if __name__ == '__main__':
	unittest.main()
