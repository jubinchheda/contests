# your code goes here

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
	#print i,j,k,M,N
	#print result
	matchChar = paramList[i][j]
	#print matchChar
	for p in xrange(i+1, i+k-1):
		if matchChar != paramList[p][j]:
			return
	for p in xrange(j+1, j+k-1):
		if matchChar != paramList[i][p]:
			return
	for p in xrange(i+1, i+k-1):
		if matchChar != paramList[p][j+k]:
			return
	for p in xrange(j+1, j+k-1):
		if matchChar != paramList[i+k][p]:
			return
	if k >= result[0]:
		result[0]=k
		result[1][0]=i
		result[1][1]=j
		result[2]=matchChar

	

paramList=[]
for line in fileinput.input():
	paramList.append(line.rstrip())	
#print paramList

N = int(paramList[0])
M = int(paramList[1])
paramList.pop(0)
paramList.pop(0)
#print N
#print M
#print paramList

minMN = min(M,N)
#print minMN


result =[2,[0,0],paramList[0][0]]

for i in xrange(M):
	for j in xrange(N):
		for k in sorted(xrange(2, min(M-i,N-j)), reverse=True):
			addSqr(paramList, i, j, k, M, N, result)
			
print result[2]
op1=""
op1+=str(result[1][0])+","+str(result[1][1])
print op1
op2=""
op2+=str(result[1][0]+result[0])+","+str( result[1][1]+result[0])
print op2
#print result[1][0],result[1][1]
#print result[1][0]+k, result[1][1]+k
