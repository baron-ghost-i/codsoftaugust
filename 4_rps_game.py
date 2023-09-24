import tkinter as tk
from tkinter import messagebox
from enum import Enum
from random import randint

COLOR = "#4fe3c3"
FONT = ("Arial", 20)
FONT2 = ("Arial", 15)

CDICT = ["Rock", "Paper", "Scissors"]

class Choice(Enum):
	Rock = 0
	Paper = 1
	Scissors = 2

	def __lt__(self, other):
		self = self.value
		if isinstance(other, Choice):
			other = other.value
		if self in [0,2] and other in [0,2]:
			self, other = other, self
		return self < other
	
	def __gt__(self, other):
		self = self.value
		if isinstance(other, Choice):
			other = other.value
		if self in [0,2] and other in [0,2]:
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
	
	def outcome(self, player: Choice, computer: Choice) -> None:
		if player > computer:
			self.p1 += 1
			winner = player
		elif player < computer:
			self.p2 += 1
			winner = computer
		else:
			winner = None
		return (player.name, computer.name, winner)

	def play(self, ch: int):
		while True:
			comp_ch = randint(0,2)
			winner = self.outcome(Choice(ch), Choice(comp_ch))
			return winner

class App(tk.Tk):
	def __init__(self, game: RPS, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.game = game
		self.geometry("800x600")
		self.configure(bg=COLOR)
		self.gameinfo = tk.Label(text="", font = FONT, bg = COLOR)
		self.gameinfo.place(anchor="center", relx=0.5, rely=0.5)
		self.topfrm = tk.Frame(self)
		tk.Label(self.topfrm, text = "Score", font = (FONT[0], FONT[1]*2), bg=COLOR).grid(row=0,column=0, sticky="ew")
		self.Score = tk.Label(self.topfrm,
					text = f"Player \t\t{self.game.p1}\nComputer \t{self.game.p2}",
					font = FONT,
					justify="left",
					bg=COLOR
				)
		self.Score.grid(row=1,column=0, sticky="W")
		self.topfrm.place(relx=0, rely=0, anchor="nw")

	def button_press(self, ch):
		winner = self.game.play(ch)
		TEXT = f"You choose... {winner[0]}!"
		self.gameinfo.configure(text=TEXT)
		self.gameinfo.after(500, lambda: self.after(TEXT+f"\nComputer chooses... {winner[1]}!", winner))
	
	#using this function as defined below provides desired behavior	
	def after(self, text, winner):
		self.gameinfo.configure(text=text)
		
		if winner[2] is not None:
			self.Score.configure(text=f"Player: \t\t{self.game.p1}\nComputer: \t{self.game.p2}")
		
		if self.game.p1 == 10:
			response = messagebox.askyesnocancel("Game Over", "You won!\nDo you want to play again?")
			self.reset(response)
		elif self.game.p2 == 10:
			response = messagebox.askyesnocancel("Game Over", "You lost!\nDo you want to play again?")
			self.reset(response)

	def reset(self, response):
		if response is None:
			for i in self.winfo_children():
				if isinstance(i, tk.Frame):
					for j in i.winfo_children():
						j.configure(state="disabled")
				else:
					i.configure(state = "disabled")
		elif not response:
			self.destroy()
		else:
			self.game.p1 = self.game.p2 = 0
			self.Score.configure(text=f"Player: \t\t{self.game.p1}\nComputer: \t{self.game.p2}")
			self.gameinfo.configure(text="")

class GFrame(tk.Frame):
	def __init__(self, master):
		super().__init__(master, bg=COLOR)
		self.place(anchor="center", relx=0.5,rely=0.75)
		self.label = tk.Label(self, text = "What would you like to play?", font = FONT2, bg = COLOR)
		self.label.grid(row=0, columnspan=3)
		
		self.r = tk.Button(self, text="Rock", font=FONT2, height=1, width=10, command = lambda:master.button_press(0))
		self.r.grid(row=1,column=0)
		
		self.p = tk.Button(self, text="Paper", font=FONT2, height=1, width=10, command = lambda:master.button_press(1))
		self.p.grid(row=1,column=1)
		
		self.s = tk.Button(self, text="Scissors", font=FONT2, height=1, width=10, command = lambda:master.button_press(2))
		self.s.grid(row=1,column=2)

def main():
	game = RPS()
	root = App(baseName="RPSGame", game=game)
	root.title("Play Rock Paper and Scissors")
	GFrame(root)
	root.resizable(0,0)
	root.mainloop()

if __name__ == "__main__":
	main()