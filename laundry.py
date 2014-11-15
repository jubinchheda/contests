# your code goes here

import fileinput
from collections import Counter
import collections
import sys

lookupDict = {}

paramList=[]
for line in fileinput.input():
	paramList.append(line.rstrip())
	
counterDict = Counter(paramList)

orderedDict = collections.OrderedDict(sorted(counterDict.items()))

for k,val in counterDict:
   outputStr = "" + str(val) + "|" + k + "\n"
   sys.stdout.write(outputStr)
	
