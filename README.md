# Calculator - Metzudat David

Simple calculator developed in Python for basic arithmetic operations through a command-line interface (CLI).

## Features

- Addition
- Subtraction
- Multiplication
- Division
- Interactive terminal menu
- Screen clearing for Windows and Linux/macOS
- Input validation for numeric values

## Project Structure

```text
Calculator-Metzudat-David/
├── MetzudatDavid.py
└── README.md
```

## Requirements

- Python 3.x

No external libraries are required.

## Installation

```bash
git clone https://github.com/josefdaniels/Calculator-Metzudat-David.git
cd Calculator-Metzudat-David
```

## Running the Project

```bash
python MetzudatDavid.py
```

## Menu

```text
1 - Addition
2 - Subtraction
3 - Multiplication
4 - Division
0 - Exit
```

After selecting an operation, the program requests two numeric values and displays the result.

## Source Code

**Main file**

- `MetzudatDavid.py`

**Main functions**

- `clear_screen()`
- `menu_home()`
- `read_number()`
- `addition()`
- `subtraction()`
- `multiplication()`
- `division()`

## Error Handling

The application includes basic exception handling for:

- `ValueError` (invalid numeric input)
- Invalid menu selections

## Technologies

- Python 3
- Standard Library:
  - `os`
