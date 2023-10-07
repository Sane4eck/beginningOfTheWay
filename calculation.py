import math

from base import BaseClient


class Calculation(BaseClient):
    def __init__(self):
        self.var1 = self.validator_value_input(self.func_exit(input("Input number 1: ")))
        self.var2 = self.validator_value_input(self.func_exit(input("Input number 2: ")))
        self.action = self.validator_sign_input(self.func_exit(input("Input sign operation: ")))

    def validator_value_input(self, value):
        try:
            if value[:3] == "cos":
                var_output = math.cos(float(value[4:-1]))
            elif value[:3] == "sin":
                var_output = math.sin(float(value[4:-1]))
            elif value[:3] == "tan":
                var_output = math.tan(float(value[4:-1]))
            elif value[:3] == "ctg":
                var_output = 1 / math.tan(float(value[4:-1]))
            else:
                var_output = float(value)
            return var_output
        except ValueError:
            print(''' 
            --------------------------------------------------------------
            - Oops!  That was no valid number.                           -
            - Pleas input: int, float, cos(x), sin(x), tan(x), ctg(x)... -
            - Or input exit() for exit in program                        -
            --------------------------------------------------------------
            ''')
            exit()

    def validator_sign_input(self, sign_operation):
        try:
            if sign_operation in ["+", "-", "*", "/"]:
                return sign_operation
        except:
            print("Error")

    def plus(self):
        solution = self.var1 + self.var2
        return print(f"Summ = {solution}")

    def minus(self):
        solution = self.var1 - self.var2
        return print(f"Minus = {solution}")

    def multiply(self):
        solution = self.var1 * self.var2
        return print(f"Multiply = {solution}")

    def division(self):
        if (self.var2 == 0):
            return print("You can't divide by zero...")
        else:
            solution = self.var1 / self.var2
            return print(f"division = {solution}")

    def start(self):
        func_dict = {"+": "plus", "-": "minus", "*": "multiply", "/": "division"}
        getattr(self, func_dict[self.action])()


if __name__ == "__main__":
    Calculation().start()
