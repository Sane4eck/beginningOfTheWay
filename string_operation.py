from abc import ABC, abstractmethod


class BaseStringOperation(ABC):
    def __init__(self):
        self.input = input("Input: ")


class CalculationElem(BaseStringOperation):
    def len_string(self):
        print(len(self.input))


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

    def rep_counting(self, dict_elements: dict, splitting_string: str):

        for i in splitting_string:
            dict_elements[f"{i}"] += 1
        return dict_elements

    def start(self):
        split_str = self.splitting_string()
        dict_with_keys = self.creating_dictionary_by_keys(self.unique_letters(split_str))
        count_items = self.rep_counting(dict_with_keys, split_str)
        return print(count_items)
CalculationElem().len_string()
UniqueLetters().start()

