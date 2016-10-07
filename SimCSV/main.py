import sys
import csv
import matplotlib.pyplot as plt
import numpy

h1 = plt.plot([], [], 'ro')[0]
currentLine = 1
plt.ylabel("Skill")
plt.xlabel("Rating")
plt.axis([0, 5000, -15000, 15000])
heatMap = numpy.array([])

def update_line(h1, new_datax, new_datay):
	h1.set_xdata(numpy.append(h1.get_xdata(), new_datax))
	h1.set_ydata(numpy.append(h1.get_ydata(), new_datay))
	plt.draw()

file = open(sys.argv[1], 'rt', encoding="utf8")
reader = csv.reader(file)
for row in reader:
	if(currentLine == 1):
		#ignore the first line
		currentLine = 1
	else:
		#print is for debugging
		#print(row[2])
		#print(currentLine-1)
		#update_line(h1, [currentLine-1], row[2])
		update_line(h1, row[2], row[1])
		numpy.append(heatMap, [row[2]], axis=0)
		numpy.append(heatMap, [row[1]], axis=0)

	currentLine += 1

plt.savefig("output.png")
#plt.pcolormesh(heatMap)
#plt.imshow(heatMap, cmap="hot", interpolation='nearest')

plt.show()
file.close()
