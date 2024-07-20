"""
File: weather_master.py
Name: Shawn Chan
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""
EXIT = -100  # Sentinel value


def main():
	"""
	pre-condition: -
	post-condition: -
	"""
	print('\"Weather Master 4.0"!')  # \ let the " in the '' show
	temper = int(input('Next temperature: (or ' + str(EXIT) + ' to quit)? '))
	if temper == EXIT:
		print('No temperatures were entered.')
	else:
		maximum = temper
		minimum = temper
		total = 0  # total temper
		cnt = 0  # for counting avg
		cold_day_cnt = 0  # for counting cold day(s), start from 0
		while True:
			if temper == EXIT:
				break
			if temper > maximum:
				maximum = temper
			if temper < minimum:
				minimum = temper
			if temper < 16:
				cold_day_cnt += 1
			cnt += 1
			total += temper
			temper = int(input('Next temperature: (or ' + str(EXIT) + ' to quit)? '))
		avg = total / cnt
		print('Highest temperature= ' + str(maximum))
		print('Lowest temperature= ' + str(minimum))
		print('Average= ' + str(avg))
		print(str(cold_day_cnt) + ' cold day(s)')


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
