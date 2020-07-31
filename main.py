#!/usr/bin/python3
#created by Kirill Shvedov

x = "hhhooohhh"

print(x[0])
print(x[:1])
print(x[-1])

#check out if x can be read vice 
#versa in the same way or not.

def is_palindrome(x):
	if x[-1] == x[1]:
		return True
	else:
		return False


print(is_palindrome(x))
