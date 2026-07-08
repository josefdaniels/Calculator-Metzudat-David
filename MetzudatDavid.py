import os
def clear_screen( ):
	os.system('cls' if os.name == 'nt' else 'clear')


def menu_home():
    clear_screen()
    print(" David Ben-Gurion, 13/12/1949 \n")
    print(" 🇮🇱 Metzudat David🇮🇱 \n")
    print("\n Choose the operation: ")
    print(" 1 -> Addition")
    print(" 2 -> Subtraction")
    print(" 3 -> Multiplication")
	print(" 4 -> Division")
    print(" 0 -> Leave")
    
    return input("\n Enter the transaction number: ")



def read_number():
 	number1 = float(int(input("\n Enter the first number: ")))
 	number2 = float(int(input(" Enter the second number: ")))
 	return number1, number2
 
	
def addition(number1, number2):
	result = number1 + number2
	print(f"\n {number1} + {number2} = {result}")
def subtraction(number1, number2):
	result = number1 - number2
	print(f"\n {number1} - {number2} = {result}")
def multiplication(number1, number2):
	result = number1 * number2
	print(f"\n {number1} × {number2} = {result}")
def division(number1, number2):
	result = number1 / number2
	print(f"\n {number1} ÷ {number2} = {result}")
	
while True:
	try:
		
		option = menu_home()
		
		if option == "0":
			break
			
		if option in ["1", "2", "3", "4"]:
		      	try:
		      		number1, number2 = read_number()
		      	except ValueError:
		      		print("\n Enter only valid numbers")
		      		input("\n Press Space to continue")
		      		continue
		
		
		
		
		if option == "1":
			addition(number1, number2)
			
		elif option == "2":
			subtraction(number1, number2)
		
		elif option == "3":
			multiplication(number1, number2)
			
		elif option == "4":
			division(number1, number2)
		
		input('\n Press Space to continue')
		clear_screen()
		
	except ValueError:
		print("\n Invalid! Enter valid numbers only")
		input("\n Press Space to continue")
		clear_screen()
