from abc import abstractmethod
import random


class BaseListOperation:
    def __init__(self):
        self.input = self.validator(input(self.text_()))

    def text_(self):
        return "Enter the number of elements in the list: "

    def genereation_list(self, num_elements: int):
        list_ = random.sample(range(0, 100), num_elements)
        return list_

    def validator(self, input_):
        try:
            if input_ == "exit()":
                exit()
            else:
                return int(input_)
        except:
            # print(e)
            print("You are entered not integer num...")
            exit()

    @abstractmethod
    def start(self):
        pass


class BaseListOperationTwoInput(BaseListOperation):
    def __init__(self):
        text_1, text_2 = self.text_()
        self.input_1 = self.validator(input(text_1))
        self.input_2 = self.validator(input(text_2))

    def text_(self):
        return "Input_1: ", "Input_2: "

    def validator(self, input_):
        try:
            if input_ == "exit()":
                exit()
            else:
                return int(input_)
        except:
            print("You are entered not integer num...")
            exit()

    @abstractmethod
    def start(self):
        pass


# TODO: {Сгенерировать массив по заданному количеству и вывести его сумму}
class GenerationAndOutputSumList(BaseListOperation):
    def text_(self):
        return "Enter the number of elements in the list: "

    def start(self):
        list_ = self.genereation_list(self.input)
        print(
            f"""\nlist: {list_}\nsum: {sum(list_)}""")


# TODO: {Максимальное и минимальное}
class MaxMinElementsInArray(BaseListOperation):
    def start(self):
        list_ = self.genereation_list(self.input)
        print(f"""\nlist: {list_} \nmin: {min(list_)} \nmax: {max(list_)}""")


# TODO: {Создать 3 массива превратить их в один}
class JoinArray(BaseListOperation):

    def start(self):
        list_1 = self.genereation_list(self.input)
        list_2 = self.genereation_list(self.input)
        list_3 = self.genereation_list(self.input)
        combine_arrays = list_1 + list_2 + list_3  # [*list_1,*list_2,*list_3]
        print(f"""\nlist_1: {list_1} \nlist_2: {list_2} \nlist_3: {list_3} \ncombine array: {combine_arrays}  """)


# TODO: {Сгенерировать массив и отфильтровать его что бы числе были больше чем какое-то число(подсказка функция filter)}
class FilterListMoreLess(BaseListOperationTwoInput):
    def text_(self):
        return "Enter the number of elements in the list: ", "Enter a number to filter the list: "

    def start(self):
        list_ = self.genereation_list(self.input_1)
        filter_ = self.input_2
        more_elements = list(filter(lambda x: x > filter_, list_))
        less_elements = list(filter(lambda x: x <= filter_, list_))
        print(
            f"""\nlist: {list_} \nfilter: {filter_} \nmore_elements: {more_elements} \nless_elements: {less_elements}  """)


# TODO: {Сгенерировать массив и каждый элемент умножить на число( подсказка функция map)}
class GenerationArrayAndMultiplyOnNum(BaseListOperationTwoInput):
    def text_(self):
        return "Enter the number of elements in the list: ", "Enter a number to multiply the list: "

    def start(self):
        list_ = self.genereation_list(self.input_1)
        multi = self.input_2
        new_list = list(map(lambda x: x * multi, list_))
        print(f"""\nlist: {list_} \nmultiply: {multi} \nnew list: {new_list}""")


# TODO: {Сгенерировать лист. Продублировать его. Вывести два списка, но во втором поменять 3 элемент на *}
class CopyListAndReplaceThirdElements(BaseListOperation):

    def replace_third_element(self, list_: list):
        list_[2] = "*"
        return list_

    def start(self):
        list_original = self.genereation_list(self.input)
        list_copy_replace = self.replace_third_element(list_original.copy())

        print(f"""\nlist original: {list_original} \nlist copyr replace: {list_copy_replace}""")


# TODO: {Сгенерировать лист от 1 до 100 с промежутком 5. По значению вывести индекс элемента}
class DisplayElementIdByItsValue(BaseListOperation):
    def text_(self):
        return "Enter value element: "

    def start(self):
        list_ = list(range(0, 101, 5))
        id_ = list_.index(self.input) if self.input in list_ else "Value not found..."
        print(f"""\nID: {id_}""")


# TODO: {Сгенерировать лист и вставить по определённому индексу элемент}
class CreateListInsertByIndexElement(BaseListOperationTwoInput):
    def __init__(self):
        text_1, text_2, text_3 = self.text_()
        self.input = self.validator(input(text_1))
        self.input_1 = self.validator(input(text_2))
        self.input_2 = self.validator(input(text_3))

    def text_(self):
        return "Enter the number of elements in the list: ", "Enter new element list: ", "Enter ID to insert: "

    def start(self):
        list_ = self.genereation_list(self.input)
        list_new = list_.copy()
        list_new.insert(self.input_2, self.input_1)
        print(f"""\nlist: {list_} \nnew list: {list_new}""")


# TODO: {СЛ. Удалить элемент по определенному индексу.}
class DeleteElementByID(BaseListOperationTwoInput):
    def text_(self):
        return "Enter the number of elements in the list: ", "Enter ID to Delete: "

    def start(self):
        list_ = self.genereation_list(self.input_1)
        num_id = self.validator(self.input_2)
        list_new = list_.copy()
        try:
            list_new.pop(num_id)
        except:
            list_new = f"Id: {num_id} not found in list: {list_new}"
        print(f"""\nlist: {list_} \nnew list: {list_new}""")


class ClassForStartProgram(BaseListOperation):
    def text_(self):
        return "Enter task number (1 - 9): "

    def start(self):
        x = {"1": GenerationAndOutputSumList, "2": MaxMinElementsInArray, "3": JoinArray,
             "4": FilterListMoreLess,
             "5": GenerationArrayAndMultiplyOnNum, "6": CopyListAndReplaceThirdElements,
             "7": DisplayElementIdByItsValue, "8": CreateListInsertByIndexElement, "9": DeleteElementByID}
        if x.get(str(self.input)):
            x[str(self.input)]().start()
        else:
            print("There is no such task...")
            exit()


if __name__ == "__main__":
    # GenerationAndOutputSumList().start()
    # MaxMinElementsInArray().start()
    # JoinArray().start()
    # FilterListMoreLess().start()
    # GenerationArrayAndMultiplyOnNum().start()
    # CopyListAndReplaceThirdElements().start()
    # DisplayElementIdByItsValue().start()
    # CreateListInsertByIndexElement().start()
    # DeleteElementByID().start()
    ClassForStartProgram().start()
