class Animal:

    def __init__(self, name=None, animal_class=None, avg_weight=None):
        
        self.__name=name
        self.__animal_class=animal_class
        self.__avg_weight=avg_weight

    def get_name(self):
        return self.__name

    def get_animal_class(self):
        return self.__animal_class

    def get_avg_weight(self):
        return self.__avg_weight

    def set_name(self,name):
        if name!='':
            self.__name=name

    def set_animal_class(self,animal_class):
        if animal_class!='':
            self.__animal_class=animal_class

    def set_avg_weight(self,avg_weight):
        if avg_weight>0:
            self.__avg_weight=avg_weight

    def show(self):
        print(f'{self.__name}, {self.__animal_class}, {self.__avg_weight} кг')

    def get_type(self):
        if self.__avg_weight < 25:
            return 'Легкий вес'
        elif self.__avg_weight < 60:
            return 'Средний вес'
        else:
            return 'Тяжелый вес'

    def compare_animal_weight(self, animal):
        if self.__avg_weight < animal.get_avg_weight():
            return 'легче'
        elif self.__avg_weight > animal.get_avg_weight():
            return 'тяжелее'
        else:
            return 'равен'

class Menu:

    def __init__(self, first_animal, second_animal):
        self.__first_animal=first_animal
        self.__second_animal=second_animal

    def show_menu(self):
        print('1 - Создать первое животное')
        print('2 - Изменить первое животное')
        print('3 - Изменить второе животное')
        print('4 - Проверить к какой весовой категории относится животное')
        print('5 - Сравнить вес двух животных')
        print('6 - Показать информацию о животных')
        print('7 - Выход')

    def user_choice(self, choice):
        match choice:
            case 1:
                self.create_animal(self.__first_animal)
            case 2:
                self.change_animal(self.__first_animal)
            case 3:
                self.change_animal(self.__second_animal)
            case 4:
                self.weight_class()
            case 5:
                self.compare_animal_weights()
            case 6:
                self.show_animals()

            case 7:
                print('Всего х о р о ш е г о')
                return False

        return True

    def create_animal(self, animal):
        name = str(input('Введите название животного: '))
        animal_class = str(input('Введите класс животного: '))
        avg_weight = int(input('Введите средний вес животного: '))

        animal.set_name(name)
        animal.set_animal_class(animal_class)
        animal.set_avg_weight(avg_weight)

    def change_animal(self, animal):
        print('Что хотите изменить?')
        print('1 - Название')
        print('2 - Класс')
        print('3 - Средний вес')

        change_choice=int(input('Введите цифру: '))

        if change_choice==1:
            name=str(input('Введите новое название: '))
            animal.set_name(name)
        elif change_choice==2:
            animal_class=str(input('Введите новый класс: '))
            animal.set_animal_class(animal_class)
        elif change_choice==3:
            avg_weight=int(input('Введите новый средний вес: '))
            animal.set_avg_weight(avg_weight)

    def weight_class(self):
        print(f"Первое животное: {self.__first_animal.get_type()}")

        print(f"Второе животное: {self.__second_animal.get_type()}")

    def show_animals(self):
        print('Первое животное: ')

        self.__first_animal.show()

        print('Второе животное: ')

        self.__second_animal.show()

    def compare_animal_weights(self):
        answer = self.__first_animal.compare_animal_weight(self.__second_animal)
        print(f'Вес первого животного {answer} второго')


class Main:

    def run(self):
        first_animal=Animal()
        second_animal=Animal('Тигр', 'Хищник', 66)
        menu=Menu(first_animal, second_animal)

        flag=0
        while flag != 1:
            menu.show_menu()
            choice = int(input('Введите цифру: '))
            if not menu.user_choice(choice):
                flag+=1

if __name__=='__main__':
    Main().run()