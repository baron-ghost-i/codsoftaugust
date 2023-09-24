import tkinter as tk
import sqlite3
from typing import Union, TYPE_CHECKING

if TYPE_CHECKING:
	from sqlite3 import Connection

BG = "#e4d96f"

ANCHORS ={
	"right": "e",
	"left": "w"
}

class App(tk.Tk):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.geometry("800x600")
		self.configure(bg=BG)
		self.db: Union[Connection, None] = None
		self.unfinished = TDLFrame(self, "left")
		self.finished = TDLFrame(self, "right")
		self.rowconfigure(0, weight=1)
		for i in [0,1]:
			self.columnconfigure(i, weight=1)

	def connect(self, db_name: str = "./todo.db"):
		self.db = sqlite3.connect(db_name) #handles connection and initial creation of database
		self.db.cursor().execute()
		return self.db
	

class TDLFrame(tk.Frame):
	def __init__(self, master, direction, *args, **kwargs):
		super().__init__(master, *args, **kwargs)
		if direction == "left":
			c = 0
		else:
			c = 1
		self.grid(row=0, column=c, sticky="nsew", padx=10, pady=50)
		self.rowconfigure(0,weight=1)
		#for i in range(3):
		#	self.columnconfigure(i, weight=1)
		scroll = tk.Scrollbar(self)
		scroll.pack(side="right", fill="y", anchor="e")
		txt = tk.Text(self)
		txt.pack(side="left", fill="y", anchor="w")


def main():
	app = App()
	app.mainloop()

if __name__=="__main__":
	main()