import tkinter
from tkinter import scrolledtext
from Member import Member

class MemberCreator(tkinter.Toplevel):
	members = None
	memberId = None

	nameEntry = None
	isMemberPaid = None
	memberComment = None

	def __init__(self, memberId, members, master = None):
		super().__init__(master = master)
		self.members = members
		self.memberId = memberId
		self.createWindow()

	def createWindow(self):
		self.geometry("500x500")
		self.title("Club Door Manager - Member Creator")

		personalFrame = tkinter.Frame(self)
		personalFrame.pack()

		idLabel = tkinter.Label(personalFrame, text = "ID: " + self.memberId)
		nameLabel = tkinter.Label(personalFrame, text = "Name: ")
		self.nameEntry = tkinter.Entry(personalFrame)
		self.isMemberPaid = tkinter.BooleanVar()
		self.memberPaid = tkinter.Checkbutton(personalFrame, text = "Membership Paid", variable = self.isMemberPaid, onvalue = True, offvalue = False)
		idLabel.pack()
		nameLabel.pack()
		self.nameEntry.pack()
		self.memberPaid.pack()


		commentFrame = tkinter.LabelFrame(self, text="Member Comments")
		commentFrame.pack(fill="both", expand="yes")

		self.memberComment = scrolledtext.ScrolledText(commentFrame, wrap=tkinter.WORD)
		self.memberComment.pack()

		save = tkinter.Button(self, text = "Save", command = self.createMember)
		save.pack()

	def createMember(self):
		info = {}
		info["name"] = self.nameEntry.get()
		info["membershipPaid"] = self.isMemberPaid.get()
		if self.memberComment != "":
			info["comment"] = self.memberComment.get("1.0", tkinter.END)

		m = Member(self.memberId, info)
		self.members.append(m)
		self.onExit()

	def onExit(self):
		self.destroy()
