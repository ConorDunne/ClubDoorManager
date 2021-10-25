import tkinter
from tkinter import scrolledtext
from Member import Member

class MemberManager(tkinter.Toplevel):
	member = None

	def __init__(self, member, master = None):
		super().__init__(master = master)
		self.member = member
		self.createWindow()

	def createWindow(self):
		self.geometry("500x500")
		self.title("Club Door Manager - Member Manager")

		personalFrame = tkinter.Frame(self)
		personalFrame.pack()

		idLabel = tkinter.Label(personalFrame, text = "ID: " + self.member.memberId)
		if self.member.membershipPaid:
			memberPaid = tkinter.Label(personalFrame, text = "Membership: Paid")
		else:
			memberPaid = tkinter.Label(personalFrame, text = "Membership: Unpaid")
		nameLabel = tkinter.Label(personalFrame, text = "Name: " + self.member.name)
		idLabel.pack()
		nameLabel.pack()
		memberPaid.pack()


		attendFrame = tkinter.Frame(self)
		attendFrame.pack()

		attendButton = tkinter.Button(attendFrame, text = "Sign in")
		attendButton.grid(row = 0, column = 0)
		if not self.member.membershipPaid:
			membershipPayment = tkinter.Button(attendFrame, text = "Pay Membership")
			membershipPayment.grid(row = 0, column = 1)


		commentFrame = tkinter.LabelFrame(self, text="Member Comments")
		commentFrame.pack(fill="both", expand="yes")

		memberComment = scrolledtext.ScrolledText(commentFrame, wrap=tkinter.WORD)
		memberComment.insert(tkinter.END, self.member.comment)
		memberComment.pack()

		save = tkinter.Button(self, text = "Save")
		save.pack()

	def onExit(self):
		self.master.destroy()