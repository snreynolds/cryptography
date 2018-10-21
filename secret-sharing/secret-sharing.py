"""secret-sharing.py"""
import random

class SecretShare:

	def __init__(self,secret,minimum,num_shares):
		self.secret = secret
		self.minimum = minimum
		self.num_shares = num_shares
		generate_random_shares(secret, minimum, num_shares)



	def div_mod(num, denom, p):
	    '''Compute num / denom in modulo p

	    >>> div_mod(3, 5, 2)
	    1

	    '''

	    inv = find_inverse(p, denom)
	    return num * inv


	def generate_random_shares(secret, minimum, num_shares):

	    assert minimum < shares, "Minimum shares must be less than total shares)"
	    poly = [secret] + [generate_prime() for i in range(minimum)]

	    shares = [(i, poly_eval(poly, i)) for i in range(1, num_shares + 1)]

	    return shares


	def poly_eval(poly, x):
	    '''Evaluate a polynomial (represented as a list) at x

	    >>> poly_eval([1, 2, 3], 4)
	    57

	    >>> poly_eval([50, 60, 70], 2)
	    450

	    '''
	    sum, i = 0, 0
	    for coef in poly:
	    	sum += coef * pow(x, i)
	    	i += 1
	    return sum

	def lagrange_interpolation(pairs):
		'''Find the polynomial P, with degree i -1 given a set of i number of points in pairs'''
		list_of_x = []
		list_of_y = []
		for x in len(pairs):
			list_of_x = list_of_x + x[0]
		for y in len(pairs):
			list_of_y = list_of_y + y[1]


