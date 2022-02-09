import json

import tkinter
from tkinter import filedialog as fd
from tkinter import messagebox

from Member import Member
from MemberManager import MemberManager
from MemberCreator import MemberCreator
from MemberList import MemberList

from NFC_Reader import ReadCard

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
		memberSearch = tkinter.Button(searchFrame, text = "Search", command = self.memberSearchID)
		memberCard = tkinter.Button(searchFrame, text = "Scan Card", command = self.memberSearchCard)
		search.grid(row = 0, column = 0)
		self.memberID.grid(row = 0, column = 1)
		memberSearch.grid(row = 0, column = 2)
		memberCard.grid(row = 0, column = 3)

		manageFrame = tkinter.Frame(self.master)
		manageFrame.pack()

		newMember = tkinter.Button(manageFrame, text = "New Member", command = self.createMember)
		barcode = tkinter.Button(manageFrame, text = "Barcode Reader")
		listMembers = tkinter.Button(manageFrame, text = "List Members", command = self.viewMemberList)
		newMember.grid(row = 1, column = 0)
		barcode.grid(row = 1, column = 1)
		listMembers.grid(row = 1, column = 2)

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
	
	def memberSearchID(self):
		found = False
		id = self.memberID.get()

		for m in self.members:
			if m.memberId == id:
				window = MemberManager(m, self.master)
				found = True
				break
	
		if not found:
			messagebox.showinfo("Error","User not found")

	def memberSearchCard(self):
		found = False
		card = ReadCard()

		for m in self.members:
			membersCards = m.card
			for c in membersCards:
				if card == c:
					window = MemberManager(m, self.master)
					found = True
					break
	
		if not found:
			messagebox.showinfo("Error","User not found")
	
	def createMember(self):
		if not self.members:
			window = MemberCreator("0", self.master, self.master)
		else:
			m = self.members[-1].memberId
			id = str(int(m)+1)
			window = MemberCreator(id, self.members, self.master)
		
	def viewMemberList(self):
		window = MemberList(self.members, self.master)