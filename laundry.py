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
#print counterDict


orderedDict = collections.OrderedDict(sorted(counterDict.items()))
#print orderedDict

for k,val in orderedDict.items():
   outputStr = "" + str(val) + "|" + k + "\n"
   sys.stdout.write(outputStr)
	
