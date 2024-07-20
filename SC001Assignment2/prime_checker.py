"""
File: prime_checker.py
Name:
-----------------------
This program asks our user for input and checks if the input is a
prime number or not. First, ” Welcome to the prime checker” will be printed on Console.
And the program will continually ask the user to enter an integer 
that is greater than 1 and checks if it is a prime number.
The program ends when the user enter the EXIT number.
"""
EXIT = -100  # Sentinel value


def main():
	"""
	pre-condition: -
	post-condition: -
	"""

	while True:
		print('Welcome to the prime checker')
		number = int(input('n: '))
		if number == EXIT:
			print('Have a good one !')
			break
		else:
			if is_prime(number):
				print(str(number) + ' is a prime number.')
			else:
				print(str(number) + ' is not a prime number.')


def is_prime(n):
	"""
	: param n: int, an integer that is greater than 1
	: return : bool, True if n is a prime number; False if n is not a prime number
	"""
	for i in range(2, n, 1):
		if n % i == 0:
			return False
	return True


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
