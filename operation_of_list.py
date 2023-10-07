from random import *

from base import BaseClient


class Operation_of_list(BaseClient):
    def __init__(self):
        self.input_count = self.validator_input_count(self.func_exit(input("Enter the count elements of list: ")))
        self.action = self.validator_action(self.func_exit(input(
            "Enter aye you action (print_list, sum_elements_list, average_value, median or exit: ")))

    def validator_input_count(self, value):
        try:
            return int(value)
        except ValueError:
            print(''' 
                        ----------------------------------------------------------------------------------------------
                        -----You are should input: (print_list, sum_elements_list, average_value, median or exit)-----
                        ----------------------------------------------------------------------------------------------
                        ''')
            exit()

    def validator_action(self, action):
        if action in ["print_list", "sum_elements_list", "average_value", "median"]:
            return action
        else:
            exit()

    def print_list(self, my_list):
        print(my_list)

    def sum_elements_list(self, my_list):
        print(sum(my_list))

    def average_value(self, my_list):
        print(sum(my_list) / len(my_list))

    def median(self, my_list):
        print(list(my_list)[int(len(my_list) / 2)])

    def start(self):
        my_list: list[int] = [randrange(0, 1000, 1) for i in range(self.input_count)]
        # my_list = []
        # for i in range(self.input_count):
        #     my_list.append(randrange(0,1000,1))
        getattr(self, self.action)(my_list)
        # self.average_value(my_list)


if __name__ == "__main__":
    Operation_of_list().start()
