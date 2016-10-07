from tkinter import *
from tkinter.filedialog import askopenfile
import csv
import matplotlib.pyplot as plt
import numpy

fileName = "No File Currently Open"
h1 = plt.plot([], [], 'ro')[0]
plt.ylabel("Skill")
plt.xlabel("Rating")
plt.axis([0, 5000, -15000, 15000])

class Window(Frame):
	def __init__(self, master = None):
		Frame.__init__(self, master)

		self.master = master

		self.init_window()

		self.currentLine = 1

	def init_window(self):
		self.master.title("Read CSV")

		self.pack(fill=BOTH, expand=1)

		quitButton = Button(self, text="Exit", command=self.client_exit)
		quitButton.place(x=270,y=0)

		openButton = Button(self, text="Open CSV", command=self.open_csv)
		openButton.place(x=0,y=0)

		runButton = Button(self, text="Run", command=self.run_analysis)
		runButton.place(x=0,y=25)

		self.fileLabel = Label(self, text=fileName)
		self.fileLabel.place(x=65,y=2)

	def client_exit(self):
		exit()

	def open_csv(self):
		root.file = askopenfile()
		self.fileName = root.file.name
		print("Opened " + self.fileName)
		self.reader = csv.reader(root.file)
		self.fileLabel['text'] = self.fileName

	def update_line(self, h1, new_datax, new_datay):
		h1.set_xdata(numpy.append(h1.get_xdata(), new_datax))
		h1.set_ydata(numpy.append(h1.get_ydata(), new_datay))
		plt.draw()

	def run_analysis(self):
		for row in self.reader:
			if(self.currentLine == 1):
				#ignore the first line
				self.currentLine = 1
			else:
				#print is for debugging
				#print(row[2])
				#print(currentLine-1)
				#update_line(h1, [currentLine-1], row[2])
				self.update_line(h1, row[2], row[1])

			self.currentLine += 1

		plt.savefig("output.png")
		plt.show()
		file.close()

root = Tk()
root.geometry("300x50")

app = Window(root)

root.mainloop()
