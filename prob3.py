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

k = long(paramsList[0])
print k

list1 = primes(k)
list2 = list(list1)
print list1
print list2
