import math


class Calculation:
    def __init__(self, var1=1, var2=1):
        self.var1 = var1
        self.var2 = var2

    def plus(self):
        decid = self.var1 + self.var2
        return print(f'Summ = {decid}')

    def minus(self):
        decid = self.var1 - self.var2
        return print(f'Minus = {decid}')

    def multiply(self):
        decid = self.var1 * self.var2
        return print(f'Multiply = {decid}')

    def division(self):
        if (self.var2 == 0):
            return print("You can't divide by zero...")
        else:
            decid = self.var1 / self.var2
            return print(f'division = {decid}')

    def checking_value_input(var_input):
        if var_input == 'exit()':
            exit()
        try:
            if (var_input[:3] == "cos"):
                var_output = math.cos(float(var_input[4:-1]))
            elif (var_input[:3] == "sin"):
                var_output = math.sin(float(var_input[4:-1]))
            elif (var_input[:3] == "tan"):
                var_output = math.tan(float(var_input[4:-1]))
            elif (var_input[:3] == "ctg"):
                var_output = 1 / math.tan(float(var_input[4:-1]))
            else:
                var_output = float(var_input)
            return var_output
        except ValueError:
            print(''' 
            --------------------------------------------------------------
            - Oops!  That was no valid number.                           -
            - Pleas input: int, float, cos(x), sin(x), tan(x), ctg(x)... -
            - Or input exit() for exit in program                        -
            --------------------------------------------------------------
            ''')
            exit(Calculation.determinate_value())

    def checking_sign_input(self, sign_operation):
        if sign_operation == 'exit()':
            exit()

        if sign_operation == "+":
            Calculation.plus(self)
            return True
        elif sign_operation == "-":
            Calculation.minus(self)
            return True
        elif sign_operation == "*":
            Calculation.multiply(self)
            return True
        elif sign_operation == "/":
            Calculation.division(self)
            return True
        else:
            print("You are should input: '+', '-', '*', '/' or 'exit()'")
            return False

    def determinate_value():
        while True:
            var_input_1 = input('Input number 1: ')
            var1 = Calculation.checking_value_input(var_input_1)

            var_input_2 = input('Input number 2: ')
            var2 = Calculation.checking_value_input(var_input_2)

            exemplar_class_calculation = Calculation(var1=var1, var2=var2)
            bool_var = True
            while bool_var == True:
                sign_operation = input('Input sign operation: ')
                sign = Calculation.checking_sign_input(exemplar_class_calculation, sign_operation)
                if sign == True:
                    bool_var = False


Calculation.determinate_value()
