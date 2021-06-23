class  Error:
    def __init__(self, *args):
        self.my_list = []

    def my_num(self):
        while True:
            try:
                val = int(input('Введите число: '))
                self.my_list.append(val)
            except:
                print(f"Вы ввели данные типа 'str'!")
                stop = input('Продолжаем? Y/n')
                if stop == 'Y' or stop == 'y':
                    print(str_error.my_num())
                else:
                    return f'Выход из программы. Текущий список - {self.my_list} \n '
                break

str_error = Error()
print('Создаем  список ваших чисел')
print(str_error.my_num())