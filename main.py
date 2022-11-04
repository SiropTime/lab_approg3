from utils import evaluate
from constants import WELCOME_MESSAGE

import sys


def enter_kwargs() -> dict:
    print("Enter variables (such as a, b, x) for expression in a row \n(a 5)\n(x 4) etc."
          "\nTo finish entering send empty string.")
    res_kwargs = {}
    while True:
        temp_tup = input().split()
        if not len(temp_tup):
            break
        elif len(temp_tup) == 2:
            try:
                res_kwargs[temp_tup[0]] = float(temp_tup[1])
            except ValueError:
                print("Enter the valid number for variable", file=sys.stderr)
        else:
            print("Enter the valid count of elements (there should be pair)", file=sys.stderr)

    return res_kwargs


def main():
    print(WELCOME_MESSAGE)

    while True:
        print("Enter the math expression: ", sep="")
        expression = str(input())

        if not len(expression.split()):
            sys.exit(0)
            
        try:
            print(evaluate(expression, **enter_kwargs()))
        except Exception as ex:
            print("The string is not math expression!", file=sys.stderr)


if __name__ == "__main__":
    main()

