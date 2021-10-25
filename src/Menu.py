import json
import tkinter
from tkinter import filedialog as fd
from tkinter import messagebox
from Member import Member
from MemberManager import MemberManager
from MemberCreator import MemberCreator

class MenuWindow(tkinter.Tk):
	members = None
	memberID = None

	def __init__(self, master=None):
		self.members = []
		self.master=master
		self.createWindow()

	def createWindow(self):
		self.master.geometry('400x100')

		ioFrame = tkinter.Frame(self.master)
		ioFrame.pack()

		importFile = tkinter.Button(ioFrame, text = "Import", command = self.importJson)
		exportFile = tkinter.Button(ioFrame, text = "Export", command = self.exportJson)
		importFile.grid(row = 1, column = 0)
		exportFile.grid(row = 1, column = 1)


		searchFrame = tkinter.Frame(self.master)  
		searchFrame.pack()

		search = tkinter.Label(searchFrame, text = "Member ID")  
		self.memberID = tkinter.Entry(searchFrame)		
		memberSearch = tkinter.Button(searchFrame, text = "Search", command = self.memberSearch)
		search.grid(row = 0, column = 0)
		self.memberID.grid(row = 0, column = 1)
		memberSearch.grid(row = 0, column = 2)


		manageFrame = tkinter.Frame(self.master)
		manageFrame.pack()

		newMember = tkinter.Button(manageFrame, text = "New Member", command = self.createMember)
		barcode = tkinter.Button(manageFrame, text = "Barcode Reader")
		newMember.grid(row = 1, column = 0)
		barcode.grid(row = 1, column = 1)

	def onExit(self):
		self.master.destroy()

	def importJson(self):
		filename = fd.askopenfilename()
		
		with open(filename, 'r') as file:
			data = file.read()
		
		obj = json.loads(data)

		for info in obj:
			self.members.append(Member(info, obj[info]))
	
	def exportJson(self):
		filename = fd.asksaveasfilename()
		out = {}

		for m in self.members:
			out[m.memberId] = m.toJson()

		jsonFile = json.dumps(out)

		f = open(filename, "w")
		f.write(jsonFile)
		f.close()
	
	def memberSearch(self):
		found = False
		id = self.memberID.get()

		for m in self.members:
			if m.memberId == id:
				window = MemberManager(m, self.master)
				found = True
				break
	
		if not found:
			messagebox.showinfo("Error","User not found")  
	
	def createMember(self):
		if not self.members:
			window = MemberCreator("0", self.master)
		else:
			m = self.members[-1].memberId
			window = MemberCreator(str(int(m)+1), self.master)