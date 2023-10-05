from Calculation import Calculation
from Notation import Notation
from Operation_of_list import Operation_of_list
from base import BaseClient


class Implementation_project(BaseClient):
    def __init__(self):
        self.func_name = self.validator_func_name(self.func_exit(
            input("Enter what are to do (calculation, notation, operation_of_list or exit()): ")))

    def validator_func_name(self, func_name):
        if func_name in ["calculation", "notation", "operation_of_list"]:
            return func_name
        else:
            exit()
    def calculation(self):
        Calculation().start()
    def notation(self):
        Notation().start()
    def operation_of_list(self):
        Operation_of_list().start()

    def start(self):
        getattr(self, self.func_name)()


if __name__ == "__main__":
    while True:
        Implementation_project().start()
