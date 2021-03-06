import tkinter
from tkinter import scrolledtext
from tkinter import messagebox
from Member import Member
from datetime import date

from NFC_Reader import ReadCard

class MemberManager(tkinter.Toplevel):
	member = None

	memberComment = None
	membershipPaid = None
	signedIn = None

	def __init__(self, member, master = None):
		super().__init__(master = master)
		self.member = member
		self.membershipPaid = self.member.membershipPaid

		today = str(date.today())
		if today not in self.member.attended:
			self.signedIn = False
		else:
			self.signedIn = True
		
		self.createWindow()

	def createWindow(self):
		self.geometry("500x600")
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

		if not self.signedIn:
			attendButton = tkinter.Button(attendFrame, text = "Sign in", command = self.memberSignedIn)
			attendButton.pack()

		assignButton = tkinter.Button(attendFrame, text = "Assign card", command = self.assignMembershipCard)

		if not self.member.membershipPaid:
			membershipPayment = tkinter.Button(attendFrame, text = "Pay Membership", command = self.membershipPaymentMade)
			membershipPayment.pack()
		assignButton.pack()

		commentFrame = tkinter.LabelFrame(self, text="Member Comments")
		commentFrame.pack(fill="both", expand="yes")

		self.memberComment = scrolledtext.ScrolledText(commentFrame, wrap=tkinter.WORD)
		self.memberComment.insert(tkinter.END, self.member.comment)
		self.memberComment.pack()

		save = tkinter.Button(self, text = "Save", command = self.saveMember)
		save.pack()
	
	def memberSignedIn(self):
		self.signedIn = True
	
	def membershipPaymentMade(self):
		self.membershipPaid = True

	def saveMember(self):
		self.member.comment = self.memberComment.get("1.0", tkinter.END)
		self.member.membershipPaid = self.membershipPaid

		if self.signedIn:
			today = str(date.today())
			if today not in self.member.attended:
				self.member.attended.append(today)
			else:
				messagebox.showinfo("Error","User already logged in today")  

		self.onExit()

	def assignMembershipCard(self):
		card = ReadCard()
		self.member.card.append(card)

	def onExit(self):
		self.destroy()