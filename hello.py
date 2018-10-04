xchange = ([2, 8, 10]) 	#variable xchange that contains a list
def double(numbs):    #function double that contains an argument numbs
	#xchange = ([2, 8, 10])
	#print xchange
	result = []			#Empty list named result
	for element in numbs:   #for loop that runs through each integer in argument numbs
		result = result + [element / 2.0]     #Divides the each integer in the list, divides them by 2 and returns them to result
	print result    #prints the final list for result

double([4, 12, 10])			#the list replaces the arguments numbs and runs through each int, should return [2.0, 6.0, 5.0]
double(xchange)				#the variable created in line 1 is used as an argument, should print [1.0, 4.0, 5.0]
j = double([2,5,6])         #the value is returned into a variable y and the result is printed, shoyld print [1.0, 2.5, 3.0]
