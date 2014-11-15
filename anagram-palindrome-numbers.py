# your code goes here
from collections import Counter
import math
import fileinput

def isPalPossible(inStr):
   stringLen = len(inStr)
   totalComb = stringLen /2
   allowedMid = 0
   if stringLen % 2 == 1:
      allowedMid = 1
   #print "allowedMid", allowedMid
   listChar =[]
   for charx in inStr:
      listChar.append(charx)
      dictum = Counter(listChar)
   numOdds = 0
   possiblePals = 0
   
   oddChar = ""
   for k, val in dictum.items():
      if val%2 == 1:
         numOdds += 1
         oddChar = k
         #print "oddChar", oddChar
         #print "numOdds", numOdds
         if numOdds >allowedMid:
         	return 0
   dictum.pop(oddChar, None)
   runningProduct = math.factorial(totalComb)
   #print "runningProduct", runningProduct
   #print runningProduct
   #print dictum
   for k, val in dictum.items():
      runningProduct/=math.factorial(val/2)
   return runningProduct
   
   
      
#print isPalPossible("abbba")
#Maain
def main():
   paramList =[]
   for line in fileinput.input():
      paramList.append(line.rstrip())
   print isPalPossible(paramList[0])
   
main()
