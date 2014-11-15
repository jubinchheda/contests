# your code goes here

import fileinput
from collections import Counter
import collections
import sys

lookupDict = {}

paramList=[]
for line in fileinput.input():
	paramList.append(line.rstrip().lower())
	
counterDict = Counter(paramList)
#print counterDict


orderedDict = collections.OrderedDict(sorted(counterDict.items()))
#print orderedDict

for k,val in orderedDict.items():
   putVal = val
   outputStr = ""
   if "sock" in k:
      putVal/=2
      if putVal >0:
         outputStr += "" + str(putVal) + "|" + k + "\n"
      if val%2 == 1:
         outputStr += "" + str(0) + "|" + k + "\n"
   else:
      outputStr += "" + str(putVal) + "|" + k + "\n"
   sys.stdout.write(outputStr)
	
