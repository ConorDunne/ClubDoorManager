import tkinter
from tkinter import ttk
from datetime import date

class MemberList(tkinter.Toplevel):
	members = None

	def __init__(self, members, master = None):
		super().__init__(master = master)
		self.members = members
		self.createWindow()

	def createWindow(self):
		self.geometry("360x225")
		self.title("Member List")

		displayFrame = tkinter.Frame(self)
		displayFrame.pack()
		
		table = ttk.Treeview(self)
		table.pack()

		table['columns'] = ("Member ID", "Member Name", "Is Signed In")
		table.column("#0", width=0,  stretch=tkinter.NO)
		table.column("Member ID",anchor=tkinter.CENTER, width=100)
		table.column("Member Name",anchor=tkinter.CENTER, width=160)
		table.column("Is Signed In",anchor=tkinter.CENTER, width=100)

		table.heading("#0",text="",anchor=tkinter.CENTER)
		table.heading("Member ID",text="Member ID",anchor=tkinter.CENTER)
		table.heading("Member Name",text="Member Name",anchor=tkinter.CENTER)
		table.heading("Is Signed In",text="Is Signed In",anchor=tkinter.CENTER)

		m = sorted(self.members, key=lambda x: x.name, reverse=False)

		for i, m in enumerate(m):
			dates = m.attended
			today = str(date.today())

			if today in dates:
				v = (m.memberId, m.name, "Yes")
			else:
				v = (m.memberId, m.name, "No")

			table.insert(parent='',index='end',iid=i,text='', values=v)

	def onExit(self):
		self.destroy()