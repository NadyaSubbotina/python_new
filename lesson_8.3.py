"""
3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
Проверить работу исключения на реальном примере. Запрашивать у пользователя данные и заполнять список
необходимо только числами. Класс-исключение должен контролировать типы данных элементов списка.
Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно,
пока пользователь сам не остановит работу скрипта, введя, например, команду «stop».
При этом скрипт завершается, сформированный список с числами выводится на экран.
Подсказка: для этого задания примем, что пользователь может вводить только числа и строки.
Во время ввода пользователем очередного элемента необходимо реализовать проверку типа элемента.
Вносить его в список, только если введено число. Класс-исключение должен не позволить пользователю
ввести текст (не число) и отобразить соответствующее сообщение. При этом работа скрипта не должна завершаться.
"""


class OnlyNumbers(Exception):
    def __init__(self):
        pass


class Validation:
    def __init__(self, *args):
        self.my_list = []

    def my_input(self):
        while True:
            try:
                try:
                    val = int(input('Введите число или Q для выхода: '))
                    self.my_list.append(val)
                    if val == 'Q' or val == 'q':
                        print(f'Итоговый список: {self.my_list} \n ')
                        break
                except ValueError:
                    raise OnlyNumbers
            except OnlyNumbers:
                print(f"Это не число!")
                y_or_n = input(f'Попробовать еще раз? Y/N ')
                if y_or_n == 'N' or y_or_n == 'n':
                    return f'Итоговый список: {self.my_list} \n '
                else:
                    self.my_input()


try_except = Validation(1)
print(try_except.my_input())
