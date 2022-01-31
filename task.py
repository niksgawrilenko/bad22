import statistics
import time
timer = time.time()
text = open('../10m.txt', 'r').readlines()
lines = []
for line in text:
    lines.append(int(line))
maxNumber = max(lines)
minNumber = min(lines)
median = statistics.median(lines)

average = statistics.mean(lines)
print("Max number:", maxNumber)
print("Min number:", minNumber)
print("Median:", median)
print("Average:", average)

indexesMax=[]
firstMax=0
lensMax=0

for index in range(len(lines)):
	if lines[index-1]<lines[index]:
    		indexesMax.append(index-1)
	else:
		indexesMax.append(index-1)
		if len(indexesMax)>lensMax:
			lensMax=len(indexesMax)
			firstMax=indexesMax[0]
			indexesMax=[]
		else:
			indexesMax=[]
print("Max sequence:",lines[firstMax:firstMax+lensMax])

indexesMin=[]
firstMin=0
lensMin=0

for index in range(len(lines)):
	if lines[index-1]>lines[index]:
    		indexesMin.append(index-1)
	else:
		indexesMin.append(index-1)
		if len(indexesMin)>lensMin:
			lensMin=len(indexesMin)
			firstMin=indexesMin[0]
			indexesMin=[]
		else:
			indexesMin=[]
print("Min sequence:",lines[firstMin:firstMin+lensMin])

print("time taken:", time.time()-timer)
