1"""
File: quadratic_solver.py
Name: Shawn Chan
-----------------------
This program should implement a console program
that asks 3 inputs (a, b, and c)
from users to compute the roots of equation:
ax^2 + bx + c = 0
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""
import math


def main():
	"""
	pre-condition:
    post-condition: According to the inputs calculate the roots of equation.
	"""
	print("stanCode QuadraticSolver!")
	a = float(input('Enter a '))
	b = float(input('Enter b '))
	c = float(input('Enter c '))
	d = b**2-4*a*c

	if d < 0:
		print('No real roots')
	elif d == 0:
		x1 = -b/(2*a)
		print('One root:', x1)
	else:  # discriminant > 0
		y = math.sqrt(d)
		x1 = (-b+y) / (2*a)
		x2 = (-b-y) / (2*a)
		print('Two roots:', x1, x2)


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
