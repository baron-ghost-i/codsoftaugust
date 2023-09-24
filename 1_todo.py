import tkinter as tk
import sqlite3
from tkinter import messagebox as mb, simpledialog as sd
from typing import Union, TYPE_CHECKING

if TYPE_CHECKING:
	from sqlite3 import Cursor 

BG = "#faf1ac"
TITLEFONT = ["Courier New", 20]
BODYFONT = ["Times New Roman", 15]
BUTTONFONT = ["Arial", 15, "bold"]

ANCHORS ={
	"right": "e",
	"left": "w"
}

class App(tk.Tk):

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.geometry("800x600")
		self.title("To Do List")
		self.configure(bg=BG)

		cursor = self.connect().cursor()
		
		self.unfinished = TDLFrame(self, "left")
		self.finished = TDLFrame(self, "right")
		self.buttons = ButtonFrame(self, self.unfinished.lb, self.finished.lb)

		self.rowconfigure(0, weight=1)
		for i in [0,2]:
			self.columnconfigure(i, weight=1)

		self.unfinished.populate(cursor)
		self.finished.populate(cursor)

	#handles connection and initial creation of database
	def connect(self, db_name: str = "todo.db"): 
		self.db = sqlite3.connect(db_name) 
		cur = self.db.cursor()
		
		#checking if table is made
		cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='todo';")
		result = cur.fetchone()
		if result is None:
			cur.execute("""
				create table todo(
					id int unique,
					desc varchar(200),
					comp int
				);
			   """)
			self.db.commit()

		return self.db
	

class TDLFrame(tk.Frame):

	def __init__(self, master: tk.Widget, direction: str, *args, **kwargs):
		super().__init__(master, *args, **kwargs)

		self.c = 2
		title = "Done"
		if direction == "left":
			self.c = 0
			title = "To Do"

		tk.Label(self, text=title, bg=BG, font=TITLEFONT).pack(side="top", fill="x")
		self.lb= tk.Listbox(self, width=200)
		self.grid(row=0, column=self.c, sticky="nsew", padx=10, pady=30)
		self.rowconfigure(0,weight=1)

		yscroll = tk.Scrollbar(self, command=self.lb.yview)
		yscroll.pack(side="right", fill="y", anchor="e")

		xscroll = tk.Scrollbar(self, command=self.lb.xview, orient="horizontal")
		xscroll.pack(side="bottom", fill="x", anchor="s")


		self.lb.pack(side="left", fill="y", anchor="w")
		self.lb['yscrollcommand'] = yscroll.set
		self.lb['xscrollcommand'] = xscroll.set

	def populate(self, cur: "Cursor"):
		cur.execute(f"select * from todo where comp  = {self.c}")
		result = cur.fetchall()
		for i in result:
			self.lb.insert(i[0], i[1])


class ButtonFrame(tk.Frame):
	
	def __init__(self, master, lb1: tk.Listbox, lb2: tk.Listbox, *args, **kwargs):
		super().__init__(master, *args, **kwargs)
		self.grid(row=0, column=1)
		self.config(bg=BG)
		self.lb1 = lb1
		self.lb2 = lb2
		
		buttonkwargs = {"font":BUTTONFONT, "width":10, "height":1, "border":2}
		
		add = tk.Button(self, text="Add", bg="#00ff00", command=self.add, **buttonkwargs)
		edit = tk.Button(self, text="Edit", bg="#0000ff", command=self.edit, **buttonkwargs)
		delete = tk.Button(self, text="Delete", bg="#ff0000", command=self.delete, **buttonkwargs)
		
		add.grid(row=0, column=0)
		edit.grid(row=2, column=0)
		delete.grid(row=4, column=0)
		
		#to provide spacing between buttons
		for i in range(1,5,2):
			tk.Label(self, bg=BG, height=5).grid(row=i,column=0)

	def add(self):
		new = sd.askstring("New Entry","Enter a brief description of the task (not more than 200 characters)")

	def edit(self):
		sel1 = self.lb1.curselection()
		sel2 = self.lb2.curselection()
		if (sel1 == sel2 == tuple()):
			return
		edited = sd.askstring("Edit Entry", "Update entry")

	def delete(self):
		sel1 = self.lb1.curselection()
		sel2 = self.lb2.curselection()
		if (sel1 == sel2 == tuple()):
			return
		edited = sd.askinteger("e", "e")

if __name__=="__main__":
	app = App()
	app.mainloop()