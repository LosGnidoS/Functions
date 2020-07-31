#!/usr/bin/python3
#created by Kirill Shvedov


#Even or Uneven
def is_odd(num):
	if (num % 2) == 0:
		return False

	else:
		return True

print(is_odd(5))


#Binary search algorithm
def dual_search(value, x=[]):

	names = ["John", "Kirill", "James",
	 "Andrew", "Dasha", "Parker"]

	x.sort()
	#return(x.index(value), x)
	if value not in x:
		return "Nothing Found" , x
	else:
		if value in x:
			return x.index(value), x

print(dual_search("Kirill", names))


		

