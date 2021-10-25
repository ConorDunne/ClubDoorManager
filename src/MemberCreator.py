import tkinter
from tkinter import scrolledtext
from Member import Member

class MemberCreator(tkinter.Toplevel):

	def __init__(self, memberId, master = None):
		super().__init__(master = master)
		self.createWindow(str(memberId))

	def createWindow(self, memberId):
		self.geometry("500x500")
		self.title("Club Door Manager - Member Creator")

		personalFrame = tkinter.Frame(self)
		personalFrame.pack()

		idLabel = tkinter.Label(personalFrame, text = "ID: " + memberId)
		nameLabel = tkinter.Label(personalFrame, text = "Name: ")
		nameEntry = tkinter.Entry(personalFrame)
		memberPaid = tkinter.Checkbutton(personalFrame, text = "Membership Paid")
		idLabel.pack()
		nameLabel.pack()
		nameEntry.pack()
		memberPaid.pack()


		commentFrame = tkinter.LabelFrame(self, text="Member Comments")
		commentFrame.pack(fill="both", expand="yes")

		memberComment = scrolledtext.ScrolledText(commentFrame, wrap=tkinter.WORD)
		memberComment.pack()

		save = tkinter.Button(self, text = "Save")
		save.pack()

	def onExit(self):
		self.master.destroy()
