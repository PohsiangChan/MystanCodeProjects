"""
File: coin_flip_runs.py
Name: Shawn Chan
-----------------------
This program should simulate coin flip(s)
with the number of runs input by users.
A 'run' is defined as consecutive results
on either 'H' or 'T'. For example, 'HHHHHTHTT'
is regarded as a 2-run result.
Your program should stop immediately after your
coin flip results reach the number of runs!
"""

import random as r

print('Let\'s flip a coin! ')
limit = int(input('Number of runs: '))


def main():
	"""
	TODO: Continuously toss a fair coin until the same side appears N times consecutively.
	Consecutive occurrences of the same side two or more times are still counted as one occurrence.
	"""

	ans = ''
	p_letter = ''
	num_run = 0
	repeat = False
	while True:
		if num_run == limit:
			break
		else:
			result = r.choice(['H', 'T'])
			if p_letter == '':
				p_letter = result
			# 第一個字母時
			elif result == p_letter and not repeat:
				num_run += 1
				repeat = True
			elif result == p_letter and repeat:
				pass
			# 當字母重複一次以上
			else:
				p_letter = result
				repeat = False
			ans += result
	print(ans)


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == "__main__":
	main()
