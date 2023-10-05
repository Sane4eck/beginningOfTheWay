import random
from random import *
# from Calculation import *
from Notation import Notation


class Operation_of_list:
    def input_count_elements_list(self):
        self.input_count = input("Enter the count elements of list: ")
        Notation.func_exit(self.input_count)
        Operation_of_list.checking_value_to_int(self)
        return self.input_count

    def checking_value_to_int(self):
        try:
            self.input_count = int(self.input_count)
            return self.input_count
        except ValueError:
            print(''' 
                       ------------------------------------------
                       - Oops!  That was no valid number.       -
                       - Pleas input: int...                    -
                       - Or input exit() for exit in program    -
                       ------------------------------------------
                       ''')
            return Operation_of_list.input_count_elements_list(self)

    def created_list(self):
        Operation_of_list.input_count_elements_list(self)
        self.my_list = []
        for i in range(0, self.input_count):
            self.my_list.append(randrange(0, 1000, 1))
        return self.my_list

    def action_list_input(self):
        self.action = input(
            "Enter aye you action(print_list(), sum_elements_list(), average_value(), median() or exit() or repit(): ")
        Notation.func_exit(self.action)
        Operation_of_list.action_list_doing(self)

    def action_list_doing(self):
        if (self.action == "print_list()"):
            return print(self.my_list), Operation_of_list.action_list_input(self)
        elif (self.action == "sum_elements_list()"):
            return print(sum(self.my_list)), Operation_of_list.action_list_input(self)
        elif (self.action == "average_value()"):
            return print(sum(self.my_list) / len(self.my_list)), Operation_of_list.action_list_input(self)
        elif (self.action == "median()"):
            return print(list(self.my_list)[int(len(self.my_list) / 2)]), Operation_of_list.action_list_input(self)
        elif (self.action == "repit()"):
            return Operation_of_list.execution_program_with_list(self)
        else:
            print("Error! There is no such command! Enter one of the commands below!")
            return Operation_of_list.action_list_input(self)

    def execution_program_with_list(self):
        Operation_of_list.created_list(self)
        print(self.my_list)
        Operation_of_list.action_list_input(self)


# Operation_of_list().execution_program_with_list()

