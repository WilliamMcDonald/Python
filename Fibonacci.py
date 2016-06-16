#!/usr/bin/python

option = int(input("What version would you like? 1? or 2?"))
 
if option == 1:

	n = int(input("What place element would you like to see?"))

	a = 0
	b = 1
	
	for i in range(0, n):
		temp = a
		a = b
		b = temp + b
   
	print("The " + str(n) + "th element is " + str(a))
else:
	
	n = int(input("How many elements of the sequence would you like to see?"))
	
	a = 0
	b = 1
	sequence = ""

	for i in range(0, n):
		temp = a
		a = b
		b = temp + b
		sequence = sequence + str(a) + " "
	
	print("The first " + str(n) + " elements are: " + sequence)
