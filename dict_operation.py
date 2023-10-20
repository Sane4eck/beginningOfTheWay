from abc import abstractmethod


class BaseDictClass:

    @abstractmethod
    def start(self, dict_values: dict):
        pass

    def validator(self, dict_values):
        if type(dict_values) is dict:
            return dict_values
        else:
            print("Entered not dict...")
            exit()

class BaseDictClassTwoInput(BaseDictClass):

    @abstractmethod
    def start(self, dict_values: dict, value: str):
        pass


# TODO: {СС. посчитать сумму значенй}
class SummDictValue(BaseDictClass):
    def start(self, dict_values: dict):
        result_valid = self.validator(dict_values)
        print(f"Sum: {sum(result_valid.values())}")


# TODO: {СС. создать новый словарь пробижать цкилом по этому значение "*". Однойстрочный цикл}
class RunningOnDict(BaseDictClass):
    def start(self, dict_values: dict):
        result_dict = self.validator(dict_values).copy()
        for i in result_dict.keys(): result_dict[i] = "*"
        print(result_dict)


# TODO: {СС. поменять местами ключ значение}
class ReplaceKeyValue(BaseDictClass):
    def start(self, dict_values: dict):
        dict_values = self.validator(dict_values)
        dict_result = dict()
        for key, value in dict_values.items():
            var = {f"{value}": key}
            dict_result.update(var)
        print(dict_result)


# TODO: {СС. Вывести только те ключи и значения где значение больше 10}
class OutputKeyAndValueWhoMore10(BaseDictClass):
    def start(self, dict_values: dict):
        # dict_values = self.validator(dict_values)
        # result_dict = dict()
        # for key, value in dict_values.items():
        #     if value > 10:
        #         result_dict.update({key: value})
        dict_values = self.validator(dict_values)
        result_dict = dict()
        result_dict.update((key, value) for key, value in dict_values.items() if value > 10)
        print(result_dict)


# TODO: {СС. Создать список из 5 словарей и отсортировать по значению ключа в словаре}
class SortDictByKey(BaseDictClass):
    def start(self, list_by_dict: list):
        try:
            list_result = sorted(list_by_dict, key=lambda x: x['A'])
            print(list_result)
        except:
            print("Enter error data")


# TODO: {СС. Проверить есть ли ключ, если нет вернуть *}
class CheckDictKey(BaseDictClassTwoInput):
    def start(self, dict_values: dict, key: list):
        if key in self.validator(dict_values):
            print(f"Key: {key} it is have...")
        else:
            print(f"Key: {key} not found... *")


# TODO: {СС. Поставить дефолтное значение *, но если такой ключ уже есть оставить предыдущее значение}
class CheckingKeyAndAddDefaultValue(BaseDictClassTwoInput):
    def start(self, dict_values: dict, key: str):
        if key not in self.validator(dict_values): dict_values.update({key: "*"})
        print(dict_values)


# TODO: {СС. По значению получить ключ}
class GetKeyByValue(BaseDictClassTwoInput):
    def start(self, dict_values: dict, value: str):
        value = [i for i in self.validator(dict_values) if dict_values[i] == value]
        print(value)


dict_value = {"id_0": 1, "id_1": 20, "id_2": 3, "id_3": 40, "id_4": 5}
list_by_dict = [{"A": 3}, {"A": 122}, {"A": 33}, {"A": 605}, {"A": 42}]
# SummDictValue().start(dict_value)
# RunningOnDict().start(dict_value)
# ReplaceKeyValue().start(dict_value)
# OutputKeyAndValueWhoMore10().start(dict_value)
# SortDictByKey().start(list_by_dict)
# CheckDictKey().start(dict_value, "id_2")
# CheckingKeyAndAddDefaultValue().start(dict_value, "id_2")
GetKeyByValue().start(dict_value, 20)
