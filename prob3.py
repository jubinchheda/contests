# your code goes here

# your code goes here

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

def addSqr(paramList, i, j, k, M, N, result):
	print i,j,k,M,N
	

paramList=[]
for line in fileinput.input():
	paramList.append(line.rstrip())	
#print paramList

N = int(paramList[0])
M = int(paramList[1])
paramList.pop(0)
paramList.pop(0)
print N
print M
print paramList

minMN = min(M,N)
print minMN


result =[]

for i in xrange(M):
	for j in xrange(N):
		for k in sorted(xrange(2, min(M-i,N-j)), reverse=True):
			addSqr(paramList, i, j, k, M, N, result)
			
