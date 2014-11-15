from collections import Counter
import math
import fileinput

def isPalPossible(inStr):
   stringLen = len(inStr)
   totalComb = stringLen /2
   allowedMid = 0
   if stringLen % 2 == 1:
      allowedMid = 1
   
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
         if numOdds >allowedMid:
         	return 0
   dictum.pop(oddChar, None)
   runningProduct = math.factorial(totalComb)
   #print runningProduct
   for k, val in dictdum.items():
      runningProduct/=math.factorial(val)
   return runningProduct
   
   
      
#print isPalPossible("abbba")
#Maain
def main():
   paramList =[]
   for line in fileinput.input():
      paramList.append(line.rstrip())
   print isPalPossible(paramList[0])
   
main()

