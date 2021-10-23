#!/usr/bin/python3

from tkinter import *

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


top.mainloop()