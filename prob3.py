# your code goes here
# your code goes here

# your code goes here

# your code goes here

# your code goes here

# your code goes here

import fileinput
from collections import Counter
import collections
import sys

def repeatDo(inputList):
	op = ""
	lenx = len(inputList)
	if lenx == 1:
		op+=","+str(inputList[0][0])
		inputList.pop(0)
		
	else:
		candx = paramList[0][0]
		if candx >= lenx:
			op+=","+str(inputList[0][0])
			inputList.pop(0)
		else:
			if paramList[candx][1] == 1:
				op+=","+str(inputList[0][0])
				inputList.pop(0)
			else:
				temp1 = inputList[candx][0]
				inputList[candx]=[inputList[0][0], 1]
				inputList[0]=[temp1, 0]
	return op			


paramList=[]
for line in fileinput.input():
	paramList.append([int(line.rstrip()), 0])	
#print paramList

paramList.pop(0)
opx=""
while True:
	opx+=repeatDo(paramList)
	#print paramList
	
	if not paramList:
		break
	
print opx[1:]
