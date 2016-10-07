import sys
import csv
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm

#initiate needed variables
plt.ylabel("Skill")
plt.xlabel("Rating")
plt.axis([0, 5000, -15000, 15000])
x = [0, 1]
y = [0, 1]
currentLine = 1
inx = 0
iny = 0

#open file
file = open(sys.argv[1], 'rt', encoding="utf8")
reader = csv.reader(file)

#iterate through each line, ignoring the first one
for row in reader:
	if(currentLine == 1):
		#ignore the first line
		currentLine = 1
	else:
		inx = int(row[2])
		iny = int(row[1])
		x.extend([inx])
		y.extend([iny])
	currentLine+=1

#matplotlib stuff
plt.hexbin(x, y, gridsize=300, cmap=cm.jet, bins=None)

#plt.colorbar()
plt.show()