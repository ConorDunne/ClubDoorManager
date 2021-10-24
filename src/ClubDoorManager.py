#!/usr/bin/python3

import tkinter
from Menu import MenuWindow

def main():
	root = tkinter.Tk()
	root.title("Club Door Management")
	app=MenuWindow(root)
	root.mainloop()


if __name__ == '__main__':
	main()