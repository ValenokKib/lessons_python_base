#dz_11.4, 11.5, 11.6

class Storage:
    '''Склад оргтехники'''
    print('Это склад оргтехники ver.1.0 \n')
    def __init__(self):
        self.my_storage = [] #словарь для хранения

    def reception(self):
        '''прием техники на склад'''
        while True:
            try:
                try_count = 0
                val_1 = input('ТИП УСТРОЙСТВА: ')
                val_2 = input('НАЗВАНИЕ УСТРОЙСТВА: ')
                val_3 = input('МОДЕЛЬ УСТРОЙСТВА: ')
                val_4 = int(input('КОЛ-ВО на ПРИЕМ: '))
                position = {'ID {}'.format(try_count + 1): 'ТИП УСТРОЙСТВА: {} НАЗВАНИЕ УСТРОЙСТВА: {} МОДЕЛЬ УСТРОЙСТВА:'
                    ' {} КОЛ-ВО: {}'.format(val_1, val_2, val_3, val_4)}
                self.my_storage.append(position)
            except ValueError:
                print('Ошибка ввода данных')

            stop = input('Продолжаем? Y/n')
            if stop == 'Y' or stop == 'y':
                print(b.reception())
            else:
                return f'текущий список ортехники на складе {self.my_storage}'
            break

    def transfer(self):
        '''передача техники со склада'''
        i = int(input('Введите номер подразделения для передачи: '))
        print(f'{self.my_storage.pop(0)} передан в подразделение -', i)
        return f'остаток оргтехники на складе {self.my_storage}'

class OfficeEquipment:
    '''Оргтехниика'''
    def __init__(self, tp, name, model, quantity):
        self.tp = tp
        self.name = name
        self.model = model
        self.quantity = quantity

class Printer(OfficeEquipment):
    '''принтеры'''
    def printers(self):
        return f'ТИП УСТРОЙСТВА {self.tp}\n БРЕНД: {self.name}\n МОДЕЛЬ УТРОЙСТВА: {self.model}\n ' \
               f'КОЛ-ВО ПОСТУПИВШЕЕ НА СКЛАД: {self.quantity}'

class Scaner(OfficeEquipment):
    '''сканеры'''
    def scaners(self):
        return f'ТИП УСТРОЙСТВА {self.tp} БРЕНД: {self.name} МОДЕЛЬ УТРОЙСТВА: {self.model} \n ' \
               f'КОЛ-ВО ПОСТУПИВШЕЕ НА СКЛАД: {self.quantity}'

class CopyMachine(OfficeEquipment):
    '''копировалки'''
    def copymachines(self):
        return f'ТИП УСТРОЙСТВА {self.tp} БРЕНД: {self.name} МОДЕЛЬ УТРОЙСТВА: {self.model} \n ' \
               f'КОЛ-ВО ПОСТУПИВШЕЕ НА СКЛАД: {self.quantity}'

#a = Printer('printer', 'hp', 'x23', 10)
#print(a.printers())
b = Storage()
print(b.reception())
print(b.transfer())