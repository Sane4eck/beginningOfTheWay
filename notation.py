from base import BaseClient


class Notation(BaseClient):
    def __init__(self):
        self.input = self.func_exit(input("Input number in 16 notation: "))
        self.type = self.func_exit(input("Enter type(2 or 10): "))

    def start(self):
        int_10 = self.validation_data()
        print_var = self.convert_to(int_10)
        print(print_var)

    def validation_data(self):
        try:
            input_var = int(self.input, 16)
            return input_var
        except ValueError:
            print(''' 
                        --------------------------------------------------------------
                        -----You are should input number in format to 16 notation-----
                        --------------------------------------------------------------
                        ''')
            exit()

    def convert_to(self, int_10):
        if self.type == "10":
            return int_10
        elif self.type == "2":
            return bin(int_10)
        else:
            return print("          \n      Please input 2 or 10...\n")


if __name__ == "__main__":
    Notation().start()
