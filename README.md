# Calculator-Metzudat-David

Simple calculator developed in Python for basic arithmetic operations through a command-line interface (CLI).

# Features

- Addition
- Subtraction
- Multiplication
- Division
- Interactive terminal menu
- Screen clearing for Windows and Linux/macOS
- Input validation for numeric values

# Project Structure
```
Calculator-Metzudat-David/
│
├── MetzudatDavid.py
└── README.md
```
# Requirements

- Python 3.x

No external libraries are required.

Running the Project

Clone the repository:

git clone https://github.com/josefdaniels/Calculator-Metzudat-David.git

Enter the project directory:

cd Calculator-Metzudat-David

Run the application:

python MetzudatDavid.py

Menu
```
- 1 -> Addition
 
- 2 -> Subtraction
 
- 3 -> Multiplication
 
- 4 -> Division
 
- 0 -> Leave
```
After selecting an operation, the program requests two numeric values and displays the result.

Source Code

Main file:

- "MetzudatDavid.py"

Main functions:

- "clear_screen()" - Clears the terminal screen.
- "menu_home()" - Displays the main menu.
- "read_number()" - Reads two numeric values from the user.
- "addition()" - Performs addition.
- "subtraction()" - Performs subtraction.
- "multiplication()" - Performs multiplication.
- "division()" - Performs division.

Error Handling

The application includes basic exception handling for:

- Invalid numeric input ("ValueError")
- Invalid menu selections

Technologies

- Python 3
- Standard Library ("os")

