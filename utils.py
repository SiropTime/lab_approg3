from constants import *
from stack import Stack


def parse(formula_string: str):
    """
    Parsing function
    :param formula_string: string with expression
    :return: Generator object with all numbers, operators and brackets
    """
    number = ""
    is_var = False
    for s in formula_string:
        if s in NUMBERS:
            number += s
            is_var = False
        elif s in LETTERS:
            if not is_var and not number:
                yield s
                is_var = True
            else:
                raise Exception("Variables is not one character")
        elif number:
            yield float(number)
            number = ""
            is_var = False
        if s in OPERATORS.keys() or s in BRACKETS:
            yield s
            is_var = False

    if number:
        yield float(number)


def polish_notation(parsed_formula):
    """
    Convertor from parsed expression to RPN
    :param parsed_formula: Parsed expression as generator object (from parse function)
    :return: Generator object with expression converted in reverse polish notation (postfix notation)
    """
    stack = Stack()

    for symbol in parsed_formula:
        if symbol in OPERATORS.keys():
            while stack.length and stack.last_element != "(" and OPERATORS[symbol][0] <= OPERATORS[stack.last_element][0]:
                yield stack.pop()
            stack.push(symbol)
        elif symbol == ")":
            while stack.length:
                s = stack.pop()
                if s == "(":
                    break
                yield s
        elif symbol == "(":
            stack.push(symbol)
        else:
            yield symbol
    while stack.length:
        yield stack.pop()


def calculate(polish, **__vars) -> float:
    """
    Counting expression from reverse polish notation
    :param polish: Converted RPN expression (from polish_notation func)
    :param __vars: Values for variables in expression. By default, every variable equals 1
    :return: Float with solution
    """
    stack = Stack()

    for symbol in polish:
        if symbol in OPERATORS.keys():
            y, x = stack.pop(), stack.pop()
            stack.push(OPERATORS[symbol][1](x, y))
        elif str(symbol) in LETTERS:
            stack.push(__vars.get(symbol, 1))
        else:
            stack.push(symbol)
    
    return float(stack.pop())


def evaluate(__source: str, **__vars):
    """
    Function that converts string to math expression in reverse polish notation and evaluate this
    :param __source: String with math expression
    :param __vars: Variables such as x, y, a, b (ordinary keywords arguments)
    :return: Float, result of math expression
    :raise: Exception if string doesn't contain math expression
    """
    return calculate(polish_notation(parse(__source)), **__vars)
