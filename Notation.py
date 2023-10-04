class Notation:
    def input_notation_16(self):
        self.input = input("Input number in 16 notation: ")
        Notation.func_exit(self.input)
        self.input = Notation.validation_data(self)
        self.type = input("Enter type(2 or 10): ")
        Notation.func_exit(self.type)
        self.input = Notation.convert_to(self)
        return self.input

    def validation_data(self):
        try:
            # if(self.input == "exit()"):
            #     return exit()
            input_var = int(self.input, 16)
            return input_var
        except ValueError:
            print(''' 
                        --------------------------------------------------------------
                        -----You are should input number in format to 16 notation-----
                        --------------------------------------------------------------
                        ''')
            exit(Notation.input_notation_16(self))

    def convert_to(self):
        if (self.input == "exit()"):
            return exit()
        if (self.type == "10"):
            return self.input
        elif (self.type == "2"):
            return bin(self.input)
        else:
            return print("          \n      Please input 2 or 10...\n"), Notation.start_notation_convert()

    def func_exit(self):
        if (self == "exit()"):
            return exit()

    def start_notation_convert():
        classObject = Notation()
        var_resulted = classObject.input_notation_16()
        return print(var_resulted), Notation.start_notation_convert()


Notation.start_notation_convert()
