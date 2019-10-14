


def getprimenumber(currentnum):
	if (currentnum == 2):
		print ('Prime Number is 3')
	elif (currentnum == 3):
		print ('Prime Number is 5')
	else:
		counter = 1
		while ((6 * counter + 1) <= currentnum):
			counter += 1
		if (6* counter -1 > currentnum):
			print ('Prime Number is {}'.format(6*counter-1))
		else:
			print ('Prime Number is {}'.format(6*counter+1))


num = int(input('Give the number after which you are looking for prime number:'))
getprimenumber(num)
