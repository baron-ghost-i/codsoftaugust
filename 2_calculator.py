#Basic calculator

OP = ["+", "-", "*", "/", "^"]

def main():
	while True:
		num1 = input("Enter first number: ")
		num2 = input("Enter second number: ")
		if (not num1.replace(".", "").isdigit()) or (not num2.replace(".", "").isdigit()):
			return print(f"Invalid numbers provided: \"{num1}\", \"{num2}\"")
		operator = input("Enter operator (+, -, *, -, ^): ")
		if operator not in OP:
			print(f"Invalid operator: \"{operator}\"")
			continue
		if operator == "^":
			operator = "**"
		print("Result: ", eval(num1+operator+num2))

if __name__ == "__main__":
	main()