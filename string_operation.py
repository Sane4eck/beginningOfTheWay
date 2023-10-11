from abc import ABC, abstractmethod


class BaseStringOperation(ABC):
    def __init__(self):
        self.input = self.exit(self.validator(input("Enter string: ")))

    def exit(self, input_):
        if input_ == "exit()":
            exit()
        return input_

    def validator(self, string_input):
        try:
            return string_input
        except:
            print("Error, ValueError")

    @abstractmethod
    def start(self):
        pass


class BaseStringOperationTwoInput(ABC):
    def __init__(self):
        self.input_1 = self.exit(self.validator(input(self.text_for_input()[0])))
        self.input_2 = self.exit(self.validator(input(self.text_for_input()[1])))

    @abstractmethod
    def text_for_input(self):
        return "Enter string: ", "Enter string: "

    def exit(self, input_):
        if input_ == "exit()":
            exit()
        return input_

    def validator(self, input_):
        try:
            return input_
        except:
            print("Error, ValueError")

    @abstractmethod
    def start(self):
        pass


# TODO: {1. Длина строки}
class CalculationElem(BaseStringOperation):
    def start(self):
        print(len(self.input))


# TODO: {2. Вводим строчку посчитать количество каждой буквы}
class UniqueLetters(BaseStringOperation):
    def splitting_string(self):
        splitted_string = []
        for i in self.input:
            splitted_string.append(i)
        return splitted_string

    def unique_letters(self, splitted_string):
        string_in_set = set(splitted_string)
        return string_in_set

    def creating_dictionary_by_keys(self, string_in_set):
        dict_elements = dict()
        for i in string_in_set:
            dict_elements[f"{i}"] = 0
        return dict_elements

    def rep_counting(self, dict_elements: dict, splitting_string: list):

        for i in splitting_string:
            dict_elements[f"{i}"] += 1
        return dict_elements

    def start(self):
        split_str = self.splitting_string()
        dict_with_keys = self.creating_dictionary_by_keys(self.unique_letters(split_str))
        count_items = self.rep_counting(dict_with_keys, split_str)
        print(count_items)


# TODO: {3. Ввести строку, где нужно поменять все повторяюще элементы на какой-то символ}

class ReplacingRepeatedLetters(UniqueLetters):
    def replacing_letters(self, split_str, dictionary_):
        string_my = []
        for i in split_str:
            if dictionary_[i] > 1:
                string_my.append("*")
            else:
                string_my.append(i)
        return "".join(string_my)

    def start(self):
        split_str = self.splitting_string()
        dict_with_keys = self.creating_dictionary_by_keys(self.unique_letters(split_str))
        count_items = self.rep_counting(dict_with_keys, split_str)
        new_string = self.replacing_letters(split_str, count_items)
        print(new_string)


# TODO: {4. Взять 2 строки и поменять у друг друга первые 2 буквы. Превратить в одну строчку}
class ReplacingOneAndTwoElements(BaseStringOperationTwoInput):
    def text_for_input(self):
        return "Enter string 1: ", "Enter string 2: "

    def replacing_and_join(self, string_1, string_2):
        new_string_1 = string_1[:2] + string_2[2:]
        new_string_2 = string_2[:2] + string_1[2:]
        return new_string_1 + new_string_2

    def start(self):
        print(self.replacing_and_join(self.input_1, self.input_2))


# TODO: {5. Ввести предложение и создать из этого массив (разделить по пробелам)}
class SentenceToArray(BaseStringOperation):
    def splitting_on_spaces(self, string_: str):
        return string_.split(" ")

    def start(self):
        list_for_print = self.splitting_on_spaces(self.input)
        print(list_for_print)


# TODO: {6. Ввести строчку. Вывести только гласные или негласные буквы (должен быть выбор)}
class SeparationVowelsConsonant(BaseStringOperationTwoInput):
    def __init__(self):
        self.input_1 = self.exit(self.validator(input(self.text_for_input()[0])))
        self.input_2 = self.validator_for_choice(self.exit(self.validator(input(self.text_for_input()[1]))))
    def text_for_input(self):
        return "Enter string: ", "Choice 1 for display \'Vowels\' or 2 for display \'Consonant\': "

    def validator_for_choice(self, input_):
        try:
            if input_ == "1" or input_ == "2":
                return int(input_)
            else:
                print("Error...Follow the instruction...")
                exit()
        except:
            exit()

    def sorted_by_choosing(self, input_string, input_choice):
        list_vowels = {"A", "E", "I", "O", "U", "a", "e", "i", "o", "u"}
        list_consonant = {"B", 'C', "D", 'F', "G", "H", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "W", "X",
                          "Y", "Z", "b", 'c', "d", 'f', "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v",
                          "w", "x", "y", "z"
                          }
        if input_choice == 1:
            list_by_sorted = list_vowels
        elif input_choice == 2:
            list_by_sorted = list_consonant

        string_only_vowels_or_consonant = ""
        for i in input_string:
            if i in list_by_sorted:
                string_only_vowels_or_consonant += i
        return string_only_vowels_or_consonant

    def start(self):
        var_output = self.sorted_by_choosing(self.input_1, self.input_2)
        print(var_output)


# TODO: {7. Добавить стр в середину строки.}
class AddStringInTheMiddle(BaseStringOperationTwoInput):
    def text_for_input(self):
        return "Enter string: ", "Enter string for insert: "

    def add_string_in_the_middle(self, string_1: str, string_2: str):
        num_position_for_add = int(len(string_1) / 2)
        new_string = "".join(string_1[:num_position_for_add] + string_2 + string_1[num_position_for_add:])
        return new_string

    def start(self):
        result = self.add_string_in_the_middle(self.input_1, self.input_2)
        print(result)


# TODO: {8. Остортировать стр по алфавиту}
class SortingStringByAlphabet(BaseStringOperation):
    def sort_str(self, string_: str):
        sort_list = sorted(string_)
        sort_str = "".join(sort_list)
        return sort_str

    def start(self):
        result = self.sort_str(self.input)
        print(result)


# TODO: {9. Вводим большую строку и проверяем есть ли в строка которую тоже вводим}
class DetectingReplica(BaseStringOperationTwoInput):
    def text_for_input(self):
        return "Enter string: ", "Enter string for find in first string: "

    def detect_replic(self, string_origin: str, string_part: str):
        if string_part in string_origin:
            return True
        else:
            return False

    def start(self):
        bool_var = self.detect_replic(self.input_1, self.input_2)
        if bool_var == True:
            print(f"String: \"{self.input_2}\", already have in \"{self.input_1}\"")
        else:
            print(f"String: \"{self.input_2}\", no detecting in \"{self.input_1}\"")


# TODO: {10. Берем задачу 5. Убираем 3 слово и делаем опять строчку с пробелами.}
class RemoveThirdWord(SentenceToArray):
    def remove_third_word(self, sentence_array: list):
        try:
            sentence_array.pop(2)
        except:
            print("Your string range small...")
            exit()

        return " ".join(sentence_array)

    def start(self):
        result = self.remove_third_word(self.splitting_on_spaces(self.input))
        print(result)


# TODO: {11. Ввести строку. Вывести в большом резисторе, в маленкьком и что бы только первая буква была большая.}
class ChangingCase(BaseStringOperationTwoInput):

    def text_for_input(self):
        return "Enter string: ", "Enter case (lower or upper): "

    def changing_case_in_string(self, string_: str, case_: str):
        if case_ == "lower":
            first_letter = string_[:1]
            rest_letter = string_[1:]
            return "".join(first_letter.upper() + rest_letter.lower())
        elif case_ == "upper":
            first_letter = string_[:1]
            rest_letter = string_[1:]
            return "".join(first_letter.lower() + rest_letter.upper())
        else:
            print("No such case exists...")
            exit()

    def start(self):
        result = self.changing_case_in_string(self.input_1, self.input_2)
        print(result)


class ClassForStartProgram(BaseStringOperation):
    def __init__(self):
        self.input = self.exit(self.validator(input("Enter task number (1 - 11): ")))

    def start(self):
        if self.input == "exit()":
            exit()
        elif self.input == "1":
            return CalculationElem().start()
        elif self.input == "2":
            return UniqueLetters().start()
        elif self.input == "3":
            return ReplacingRepeatedLetters().start()
        elif self.input == "4":
            return ReplacingOneAndTwoElements().start()
        elif self.input == "5":
            return SentenceToArray().start()
        elif self.input == "6":
            return SeparationVowelsConsonant().start()
        elif self.input == "7":
            return AddStringInTheMiddle().start()
        elif self.input == "8":
            return SortingStringByAlphabet().start()
        elif self.input == "9":
            return DetectingReplica().start()
        elif self.input == "10":
            return RemoveThirdWord().start()
        elif self.input == "11":
            return ChangingCase().start()
        else:
            print("There is no such task...")
            exit()


if __name__ == "__main__":
    # ChangingCase().start()
    # CalculationElem().start()
    # UniqueLetters().start()
    # ReplacingRepeatedLetters().start()
    # ReplacingOneAndTwoElements().start()
    # SentenceToArray().start()
    # SeparationVowelsConsonant().start()
    # AddStringInTheMiddle().start()
    # SortingStringByAlphabet().start()
    # DetectingReplica().start()
    # RemoveThirdWord().start()

    ClassForStartProgram().start()
