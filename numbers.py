#!/usr/bin/env python3
import array,unittest,itertools
from math import *
from time import time

def to_digits(number):
	#How many digits we have
	amount = int(ceil(log(number + 1, 10)))
	digits = []
	
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
	digits = to_digits(number)
	
	for pos in range(1, len(digits)):
		part = digits[0:pos + 1]
		number_ending = to_number(part)
		permutations = itertools.permutations(part)
		next_ending = None
		for permutation in permutations:
			ending_to_test = to_number(permutation)
			if ending_to_test > number_ending and (next_ending == None or ending_to_test < next_ending):
				next_ending = ending_to_test
				part = list(permutation)
		if next_ending != None:
			digits[0:len(part)] = part
			return to_number(digits)
	return number
		

def brute_force(number):
	digits = to_digits(number)
	permutations = itertools.permutations(digits)
	
	numbers = set()
	for permutation in permutations:
		permutation_number = to_number(permutation)
		numbers.add(permutation_number)

	#print("permutations: {}".format(len(numbers)))
	numbers = list(numbers)
	numbers.sort()
	index = numbers.index(number)
	if index + 1 >= len(numbers):
		return number
	else:
		return numbers[index + 1]
		
	

class Test(unittest.TestCase):
	def test_to_digits(self):
		digits = {11:[1,1], 4:[4], 1234:[1,2,3,4], 865320865:[8,6,5,3,2,0,8,6,5]}
		for k,v in digits.items():
			#reverse because we're indexing by digit position and not naturally
			v.reverse()
			self.assertEqual(to_digits(k), v)

	def test_next_from_same_digits(self):
		numbers = [11, 12, 123, 3244, 234, 3527563, 2234325, 652342831, 89765432, 987654321] #987654321 is a worst case
		for number in numbers:
			start = time()
			expected = brute_force(number)
			end = time()
			print("Brute force took: {}ms".format(((end - start)) * 1000))
			start = time()
			actual = next_from_same_digits(number)
			end = time()
			print("Permutations from end took: {}ms".format(((end - start) * 1000)))
			print("Brute force: {} < {}".format(number, expected))
			print("Permutations from end: {} < {}\n".format(number, actual))
			self.assertEqual(actual, expected)

	def test_brute_force(self):
		numbers = {12: 21, 342: 423, 1243: 1324}
		for number, expected in numbers.items():
			actual = brute_force(number)
			self.assertEqual(actual, expected)

if __name__ == '__main__':
	unittest.main()

