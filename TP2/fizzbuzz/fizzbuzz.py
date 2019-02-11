
x=0
while x<200:
	x=x+1
	if x%3==0 and x%5==0:
		print "FizzBuzz"
	elif x%3==0 and x%5!=0:
		print "Buzz"
	elif x%5==0 and  x%3!=0:
		print "Fizz"
	else :
		print x
