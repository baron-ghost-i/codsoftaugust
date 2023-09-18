#import tkinter as tk
from enum import Enum
from random import randint

l = [0,2]

choice = {
	"R": 0,
	"P": 1,
	"S": 2
}

class Choice(Enum):
	R = 0
	P = 1
	S = 2

	def __lt__(self, other):
		self = self.value
		if isinstance(other, Choice):
			other = other.value
		if self in l and other in l:
			self, other = other, self
		return self < other
	
	def __gt__(self, other):
		self = self.value
		if isinstance(other, Choice):
			other = other.value
		if self in l and other in l:
			self, other = other, self
		return self > other
	
	def __eq__(self, other):
		if isinstance(other, Choice):
			other = other.value
		return self.value == other

class RPS:
	def __init__(self):
		self.p1 = 0
		self.p2 = 0
	
	def outcome(self, p1: Choice, p2: Choice) -> None:
		if p1 > p2:
			self.p1 += 1
			return "p1"
		elif p1 < p2:
			self.p2 += 1
			return "p2"
		else:
			return "Draw"

	def game(self) -> None:
		while True:
			ch = input("Enter Choice (RPS): ")
			if ch in "RrPpSs":
				ch = Choice(choice[ch.upper()])

			comp_ch = randint(0,2)
			winner = self.outcome(Choice(ch), Choice(comp_ch))
			print(winner, ch.value, comp_ch, f"Score: {self.p1}:{self.p2}")
'''
class App(tk.Frame):
	def __init__(self, master):
		super().__init__(master)
		self.pack()
'''