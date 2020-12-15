"""
Author: Rawley Collins
Program: Program.py

main gui file
"""
from tkinter import *
import tkinter.messagebox
import db_connection as db

"""
3 items: a button for each to add to cart, a button to remove from cart, a counter for how many you want. all disabled until sign in
a sign up button, and a login button
a user name box, a password box. Enabled when the login button is hit
a

"""


class dbmsGUI:
	def __init__(self, window):
		self.conn = db.create_connection('customerDBMS.db')
		window.title("Local Store")
		window.geometry("800x600")
		#----
		self.startProgram = Button(text="Start Program", width=16, height=1, fg="white", bg="green", command=lambda: self.create_db_table())
		self.startProgram.grid()
		# data entry widgets
		self.userNameLabel = Label(app_window, text="Username:")
		self.passwordLabel = Label(app_window, text="Password:")
		self.userNameEntry = Entry(app_window)
		self.passwordEntry = Entry(app_window)

		# data entry placement
		self.userNameLabel.grid(row=1, sticky=E)
		self.passwordLabel.grid(row=2, sticky=E)
		self.userNameEntry.grid(row=1, column=1)
		self.passwordEntry.grid(row=2, column=1)

		# log in buttons
		self.createAccount = Button(text="Create account", width=16, height=1, fg="black")
		self.createAccount.grid(row=3, column=0)
		self.logIn = Button(text="log in", fg="white", width=16, height=1, bg="blue")
		self.logIn.grid(row=3, column=1)
		self.logOut = Button(text="log out", fg="black", width=16, height=1, bg="light gray")
		self.logOut.grid(columnspan=2, sticky=N)

		# create user buttons


	def create_db_table(self):
		db.create_tables(self.conn)
		self.startProgram.configure(state=tkinter.DISABLED)

	def create_customer(self):
		# enable input buttons
		pass

	def log_in(self):

app_window = tkinter.Tk()
store_app = dbmsGUI(app_window)
app_window.mainloop()
