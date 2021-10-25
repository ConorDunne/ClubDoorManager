import tkinter
from tkinter import ttk

class MemberList(tkinter.Toplevel):
	members = None

	def __init__(self, members, master = None):
		super().__init__(master = master)
		self.members = members
		self.createWindow()

	def createWindow(self):
		self.geometry("260x225")
		self.title("Member List")

		displayFrame = tkinter.Frame(self)
		displayFrame.pack()
		
		table = ttk.Treeview(self)
		table.pack()

		table['columns'] = ("Member ID", "Member Name")
		table.column("#0", width=0,  stretch=tkinter.NO)
		table.column("Member ID",anchor=tkinter.CENTER, width=100)
		table.column("Member Name",anchor=tkinter.CENTER, width=160)

		table.heading("#0",text="",anchor=tkinter.CENTER)
		table.heading("Member ID",text="Member ID",anchor=tkinter.CENTER)
		table.heading("Member Name",text="Member Name",anchor=tkinter.CENTER)

		for i, m in enumerate(self.members):
			table.insert(parent='',index='end',iid=i,text='', values=(m.memberId, m.name))

	def onExit(self):
		self.destroy()