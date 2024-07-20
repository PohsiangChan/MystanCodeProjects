"""
File: largest_digit.py
Name: Shawn Chan
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	:param n:
	:return:
	"""
	# 負數
	if n < 0:
		# n = -n
		return find_largest_digit(-n)

	elif n < 10:
		return n
	else:
		# 取最後一個字母
		last_num = n % 10
		# 去掉最後一個字母
		rest_largest = find_largest_digit(n // 10)
		return max(last_num, rest_largest)


if __name__ == '__main__':
	main()
