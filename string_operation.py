from abc import ABC, abstractmethod
from collections import Counter
import string


class BaseStringOperation(ABC):
    def __init__(self):
        self.input = self.exit(input(self.text_for_input()))

    def text_for_input(self):
        return "Enter string: "

    def exit(self, input_):
        if input_ == "exit()":
            exit()
        return input_

    @abstractmethod
    def start(self):
        pass


class BaseStringOperationTwoInput(ABC):
    def __init__(self):
        text1, text2 = self.text_for_input()
        self.input_1 = self.exit(input(text1))
        self.input_2 = self.exit(input(text2))

    def text_for_input(self):
        return "Enter string: ", "Enter string: "

    def exit(self, input_):
        if input_ == "exit()":
            exit()
        return input_

    @abstractmethod
    def start(self):
        pass


# TODO: {1. Длина строки}
class CalculationElem(BaseStringOperation):
    def start(self):
        print(len(self.input))


# TODO: {2. Вводим строчку посчитать количество каждой буквы}
class UniqueLetters(BaseStringOperation):
    def start(self):
        count_items = dict(Counter(self.input))
        print(count_items)


# TODO: {3. Ввести строку, где нужно поменять все повторяюще элементы на какой-то символ}

class ReplacingRepeatedLetters(BaseStringOperationTwoInput):
    def text_for_input(self):
        return "Enter string: ", "Enter letter: "

    def start(self):
        result = self.input_1.replace(self.input_2, "*")
        print(result)


# TODO: {4. Взять 2 строки и поменять у друг друга первые 2 буквы. Превратить в одну строчку}GGGOOGOFD
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
        list_vowels = 'aeiouAEIOU'
        list_consonant = ''.join(c for c in string.ascii_letters if c not in list_vowels)

        list_by_sorted = list_vowels if input_choice == 1 else list_consonant
        string_only_vowels_or_consonant = "".join( j for j in input_string if j in list_by_sorted)
        return string_only_vowels_or_consonant

    def start(self):
        self.validator_for_choice(self.input_2)
        var_output = self.sorted_by_choosing(self.input_1, self.validator_for_choice(self.input_2))
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

    def start(self):
        if self.input_2 in self.input_1:
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
        return "Enter string: ", "Enter case (lower or upper or mixed): "

    def start(self):
        if self.input_2 == "lower":
            result = self.input_1.lower()
        elif self.input_2 == "upper":
            result = self.input_1.upper()
        elif self.input_2 == "mixed":
            result = self.input_1.title()
        else:
            print("No such case exists...")
            exit()
        print(result)


class ClassForStartProgram(BaseStringOperation):
    def text_for_input(self):
        return "Enter task number (1 - 11): "

    def start(self):
        x = {"1": CalculationElem, "2": UniqueLetters, "3": ReplacingRepeatedLetters, "4": ReplacingOneAndTwoElements,
             "5": SentenceToArray, "6": SeparationVowelsConsonant, "7": AddStringInTheMiddle,
             "8": SortingStringByAlphabet, "9": DetectingReplica, "10": RemoveThirdWord, "11": ChangingCase}
        if x.get(self.input):
            x[self.input]().start()
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
