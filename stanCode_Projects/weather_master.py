"""
File: weather_master.py
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""


EXIT = -1


def main():
	"""
	This program helps circulate the highest temperature,lowest temperature,cold days(temperature<16) and average temperature.
	"""
	print('stanCode"Weather Master 4.0"!!!')
	tem = int(input('Next temperature: (or '+str(EXIT)+' to quit.)?'))
	h = tem
	l = tem
	time = 0
	cold = 0
	sum = 0
	# set up all variables
	if tem == EXIT:
		print('No temperatures were entered.')
	else:
		while not tem == EXIT:
			h = find_highest(tem, h)
			l = find_lowest(tem, l)
			time += 1
			sum = plus_all(tem, sum)
			a = average(sum, time)
			if tem < 16:
				cold += 1
			tem = int(input('Next temperature: (or ' + str(EXIT) + ' to quit.)?'))
		final(h, l, a, cold)


def find_highest(tem, h):
	"""
	:param tem:int, the temperature that user entered.
	:param h:int, the highest temperature so far.
	This function finds the highest temperature.
	"""
	max = h
	if tem > max:
		return tem
	return h


def find_lowest(tem, l):
	"""
	:param tem:int, the temperature that user entered.
	:param l:int, the lowest temperature so far.
	This function finds the lowest temperature.
	"""
	min = l
	if tem < l:
		return tem
	return l


def plus_all(tem, sum):
	"""
	:param tem:int, the temperature user entered.
	:param sum:int, the sum of temperatures user entered.
	This function plus all temperatures user entered.
	"""
	return sum+tem


def average(sum, tem):
	"""
	:param sum:int,the temperature sum
	:param tem:int, the temperature that user entered.
	This function circulate the average temperature.
	"""
	return float(sum/tem)


def final(h, l, a, cold):
	"""
	:param h: int,the highest temperature.
	:param l: int,the lowest temperature.
	:param a: int,the average temperature.
	:param cold: int,the amount of the day under 16 degrees Celsius
	This function print the final result.
	"""
	print('Highest temperature = '+str(h))
	print('Lowest temperature = '+str(l))
	print('Average = '+str(a))
	print(str(cold)+' cold days.')



###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
