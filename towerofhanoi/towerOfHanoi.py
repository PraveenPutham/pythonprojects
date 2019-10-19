
def updateDisk(fromTower, toTower, A, B, C, steps):
	if fromTower == "A":
		val = A.pop(-1)
	elif fromTower == "B":
		val = B.pop(-1)
	else:
		val = C.pop(-1)
	#print("value = {0}".format(val))
	if toTower == "A":
		A.append(val)
	elif toTower == "B":
		B.append(val)
	else:
		C.append(val)
	steps[0] = steps[0] + 1 
	return val


def moveDisk(numberOfDisks, fromTower, middleTower, toTower , A, B, C, steps):
	if numberOfDisks > 1:
		moveDisk(numberOfDisks-1, fromTower, toTower, middleTower, A, B, C, steps)
		moveDisk(1,fromTower, middleTower, toTower, A, B, C,steps)
		moveDisk(numberOfDisks-1, middleTower, fromTower, toTower, A, B, C, steps)
	else:
		val = updateDisk(fromTower, toTower, A, B, C, steps)
		#print ("val : {0} , steps: {1}". format(val, steps))
		print ("Move Disk from {0}{2} -> {1}{2}".format(fromTower, toTower, val))
	

if (__name__ == "__main__"):
	while True:
		numberOfDisks = int(input("Enter the number of Disks:"))
		if numberOfDisks < 3:
			continue
		else:
			break

	j = numberOfDisks
	A = []
	while j != 0 :
		A.append(str(j))
		j = j - 1
	B = []
	C= []
	steps = [0]
	print ("Initially Tower A contains {0}, Tower B contains {1}, Tower C contains {2}".format(A,B,C))
	moveDisk (numberOfDisks, "A", "B", "C", A, B, C, steps)
	print ("Finally Tower A contains {0}, Tower B contains {1}, Tower C contains {2}".format(A,B,C))
	print ("Total Steps: {0}".format(steps[0]))





