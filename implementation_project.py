from Calculation import Calculation
from Notation import Notation
from Operation_of_list import Operation_of_list


class Implementation_project:
    def input_selection(self):
        self.input_select = input("Enter what are to do (Calculation(), Notation(), Operation_of_list() or exit()): ")
    def checking_input(self):
        if(self.input_select == "Calculation()"):
            Calculation.determinate_value()
        elif(self.input_select == "Notation()"):
            Notation.start_notation_convert()
        elif (self.input_select == "Operation_of_list()"):
            Operation_of_list().execution_program_with_list()
        elif (self.input_select == "exit()"):
            Notation.func_exit(self)
        else:
            return print("Error! There is no such command!"), Implementation_project.satart_programm(self)

    def satart_programm(self):
        Implementation_project.input_selection(self)
        Implementation_project.checking_input(self)


Implementation_project().satart_programm()