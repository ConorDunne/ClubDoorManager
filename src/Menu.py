import tkinter

class MenuWindow(tkinter.Tk):
	def __init__(self, master=None):
		self.master=master		
		self.master.geometry('400x100')

		ioFrame = tkinter.Frame(self.master)
		ioFrame.pack()

		importFile = tkinter.Button(ioFrame, text = "Import").grid(row = 1, column = 0)
		exportFile = tkinter.Button(ioFrame, text = "Export").grid(row = 1, column = 1)

		searchFrame = tkinter.Frame(self.master)  
		searchFrame.pack()

		search = tkinter.Label(searchFrame,text = "Member ID").grid(row = 0, column = 0)  
		memberID = tkinter.Entry(searchFrame).grid(row = 0, column = 1)
		memberSearch = tkinter.Button(searchFrame, text = "Search").grid(row = 0, column = 2)

		manageFrame = tkinter.Frame(self.master)
		manageFrame.pack()

		newMember = tkinter.Button(manageFrame, text = "New Member").grid(row = 1, column = 0)
		barcode = tkinter.Button(manageFrame, text = "Barcode Reader").grid(row = 1, column = 1)

	def onExit(self):
		self.master.destroy()

	def test(self):
		print("hello")

"""

top = Tk()
top.geometry("400x250")

searchFrame = Frame(top)  
searchFrame.pack()

search = Label(searchFrame,text = "Member ID").grid(row = 0, column = 0)  
memberID = Entry(searchFrame).grid(row = 0, column = 1)
memberSearch = Button(searchFrame, text = "Search").grid(row = 0, column = 2)

manageFrame = Frame(top)
manageFrame.pack()

newMember = Button(manageFrame, text = "New Member").grid(row = 1, column = 0)
barcode = Button(manageFrame, text = "Barcode Reader").grid(row = 1, column = 1)

"""