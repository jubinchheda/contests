import fileinput


paramList =[]
for line in fileinput.input():
    paramList.append(line.rstrip())
    
    
inStr = paramList[0]

allowedMid = 0
isPal = 1
for idx in xrange(len(inStr)):
	currCount = inStr.count(inStr[idx])
	if currCount %2 == 1:
		allowedMid +=1
		if allowedMid > 1:
			isPal = 0
			break
		
if isPal == 0:
	print "no"
else:
	print "yes"
