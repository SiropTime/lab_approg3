# Dictionary with operators where key is operator and value is tuple with priority and lambda with operand's expression
OPERATORS = {
    '+': (1, lambda x, y: x + y), '-': (1, lambda x, y: x - y),
    '*': (2, lambda x, y: x * y), '/': (2, lambda x, y: x / y),
    '=': (0, lambda x, y: x == y), '^': (3, lambda x, y: x**y)
}

NUMBERS = "1234567890."
LETTERS = "qwertyuiopasdfghjklzxcvbnm"
BRACKETS = "()"


WELCOME_MESSAGE = """
                  Maltsev Timofey 2022
                  IDB-21-10 LAB 3 VAR 15

                  Check if a string is syntax correctly math expression.
                  Math expression can inclue numbers, one-length letter-variables, operators and round brackets.
                  Enter empty string to exit.
                  """
