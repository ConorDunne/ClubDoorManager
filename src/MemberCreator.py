import tkinter
from tkinter import scrolledtext
from tkinter import messagebox

from Member import Member
from NFC_Reader import ReadCard

class MemberCreator(tkinter.Toplevel):
	members = None
	memberId = None

	nameEntry = None
	isMemberPaid = None
	memberComment = None
	card = None

	def __init__(self, memberId, members, master = None):
		super().__init__(master = master)
		self.members = members
		self.memberId = memberId
		self.card = []
		self.createWindow()

	def createWindow(self):
		self.geometry("500x600")
		self.title("Club Door Manager - Member Creator")

		personalFrame = tkinter.Frame(self)
		personalFrame.pack()

		idLabel = tkinter.Label(personalFrame, text = "ID: " + self.memberId)
		nameLabel = tkinter.Label(personalFrame, text = "Name: ")
		self.nameEntry = tkinter.Entry(personalFrame)
		self.isMemberPaid = tkinter.BooleanVar()
		self.memberPaid = tkinter.Checkbutton(personalFrame, text = "Membership Paid", variable = self.isMemberPaid, onvalue = True, offvalue = False)
		self.assignCard = tkinter.Button(personalFrame, text = "Assign Card", command = self.assignMembershipCard)
		idLabel.pack()
		nameLabel.pack()
		self.nameEntry.pack()
		self.memberPaid.pack()
		self.assignCard.pack()		


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
		info["card"] = self.card

		m = Member(self.memberId, info)
		self.members.append(m)
		self.onExit()

	def assignMembershipCard(self):
		card = ReadCard()

		if card == -1:
			messagebox.showinfo("Error", "No card detected")
		else:
			print(card)
			self.card.append(card)

	def onExit(self):
		self.destroy()
