# your code goes here

import fileinput
from collections import Counter
import collections
import sys


def primes(n): 
	if n==2: return [2]
	elif n<2: return []
	s=range(3,n+1,2)
	mroot = n ** 0.5
	half=(n+1)/2-1
	i=0
	m=long(3)
	while m <= mroot:
		if s[i]:
			j=(m*m-3)/2
			s[j]=0
			while j<half:
				s[j]=0
				j+=m
		i=i+1
		m=2*i+3
	return [2]+[x for x in s if x]

paramList=[]
for line in fileinput.input():
	paramList.append(line.rstrip())	

k = long(paramList[0])
print k

list1 = sorted(primes(k), reverse=True)
#print list1
list2 = list(list1)
output1 = ""

for i in list1:
	if i-2 in list2:
	   output1+=str(i-2)+","+str(i)
	   print output1
	   break
		

	
