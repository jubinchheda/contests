import fileinput

def my_abs(list1, list2):
   sum = 0
   for i in xrange(len(list1)):
      sum+= abs(list1[i]-list2[i])
   return sum


paramList =[]
for line in fileinput.input():
    paramList.append(line.rstrip())
    
k = int(paramList[0].rstrip())

oldData =[]
for i in xrange(k):
   csvList = paramList[i+1].split(",")
   oldDataPoint = []
   for elem in csvList:
      oldDataPoint.append(float(elem.rstrip()))
   oldData.append(list(oldDataPoint))

#print oldData
	
newData = []
for i in xrange(k):
   csvList = paramList[k+i+1].split(",")
   oldDataPoint = []
   for elem in csvList:
      oldDataPoint.append(float(elem.rstrip()))
   newData.append(list(oldDataPoint))

for m in xrange(k):
   min_abs = my_abs(oldData[m], newData[0])
   min_n = 0
   for n in xrange(k):
      curr_abs = my_abs(oldData[m], newData[n])
      #print oldData[m],newData[n],curr_abs
      if curr_abs < min_abs:
         min_abs = curr_abs
         min_n = n
   print m,min_n
