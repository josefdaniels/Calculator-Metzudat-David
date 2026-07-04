import os
def limpar_tela( ):
	os.system('cls' if os.name == 'nt' else 'clear')
	


while True:
    limpar_tela( )
    print("\033[1m David Ben-Gurion, 13/12/1949\033[0m \n")
    print(" 🇮🇱 \033[1mMetzudat David\033[0m 🇮🇱 \n") 
    print("     \033[36mירושלים של זהב\033[0m")
    print("\n\033[1m Choose the operation: \033[0m")
    print("\033[1m 1 -> Addition\033[0m")
    print("\033[1m 2 -> Subtraction\033[0m")
    print("\033[1m 3 -> Multiplication\033[0m")
    print("\033[1m 4 -> Division\033[0m")
    print("\033[1m 5 -> Exponentiatiom\033[0m")
    print("\033[1m 6 -> Square Root\033[0m")
    print("\033[1m 0 -> Leave\033[0m")
    
    opcao = input("\n\033[1m Enter the transaction number:\033[0m ")
    
    if opcao == "0":
        print("\n\033[1m Shemot Gimel-Dale ✡︎ \033[m\n")
        break
      
    elif opcao == "6":
        try:
        	num = float(input("\033[1m Enther the number: \033[0m"))
        	if num < 0:
        		print("\033[1m This is no square of a negative number\033[0m")
        	else:
        		resultado = num ** 0.5
        		print(f"\033[1m √{num} = {resultado: .6f}\033[0m")
        except ValueError:
        	print("\033[1m Enter only valid numbers\033[0m")
        
    elif opcao in ["1", "2", "3", "4", "5", "6"]:
        try:
        	num1 = float(input("\033[1m Enter the first number:\033[0m "))
        	num2 = float(input("\033[1m Enter the second number:\033[0m "))
        except ValueError:
        	print("\033[1m Enter only valid numbers\033[0m")
    
        	input("\n\033[1m Press any key to continue: \033[1m")
        	continue
        if opcao == "1":
            resultado = num1 + num2
            print(f"\033[1m {num1} + {num2} = {resultado}\033[0m")
            
        elif opcao == "2":
            resultado = num1 - num2
            print(f"\033[1m {num1} - {num2} = {resultado}\033[0m")
            
        elif opcao == "3":
            resultado = num1 * num2
            print(f"\033[1m {num1} × {num2} = {resultado}\033[0m")
            
        elif opcao == "5":
            resultado = num1 ** num2
            print(f"\033[1m {num1}^{num2} = {resultado}\033[0m")
            
           
           
            
        elif opcao == "4":
            if num2 == 0:
                print("\033[1m It is not possible to divide by zero\033[0m")
            else:
                	resultado = num1 / num2
                	print(f"\033[1m {num1} ÷ {num2} = {resultado:.4f}\033[0m") 
                  
          

    else:
        print("\033[1m Invalid option! enter a number from 0 to 6\033[0m ")
        
    input("\n\033[1m Press any key to continue\033[0m ")