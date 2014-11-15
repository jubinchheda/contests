from collections import Counter
import itertools as it


def isPalPossible(inStr):
   stringLen = len(inStr)
   totalComb = stringLen /2
   allowedMid = 0
   if stringLen % 2 == 1:
      allowedMid = 1
   
   listChar =[]
   for charx in inStr:
      listChar.append(charx)
   print len(it.permutations(listChar))
   dictum = Counter(listChar)
   numOdds = 0
   possiblePals = 0
   for k, val in dictdum.items():
      if val%2 == 1:
         numOdds += 1
         if numOdds >allowedMid:
         	return 0
    
    
      
   
      
print isPalPossible("abbba")

