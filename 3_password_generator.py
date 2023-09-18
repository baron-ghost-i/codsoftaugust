#password generator

import argparse
from random import randint, choice
from string import digits, ascii_letters, punctuation

CHARS = list(ascii_letters + digits)

parser = argparse.ArgumentParser(description = "Generates a random password based on the length provided.")
parser.add_argument("-l", "--length", type = int)
parser.add_argument("-is", "--include_special", action = "store_true")

def main():
	length: int = parser.parse_args().length
	spec: bool = parser.parse_args().include_special
	if spec:
		CHARS.extend(punctuation)
	if length is None:
		try:
			length = int(input("Enter length of password to be generated: "))
		except ValueError:
			return print(f"Invalid length provided.")
		except:
			raise
	string = "".join([choice(CHARS) for i in range(length-1)])
	string = choice(CHARS)+string
	return print(string)

if __name__ == "__main__":
	main()