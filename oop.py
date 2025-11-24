class Animal:
    """
    Данный класс описывает животное
    """


    def __init__(self, name = 'NA', animal_class = 'NA', avg_weight = None) -> None:
        """
        Конструктор класса.

        :param name: Название животного.
        :param animal_class: Класс животного.
        :param avg_weight: Средний вес животного.
        """

        self.__name = name
        self.__animal_class = animal_class
        self.__avg_weight = avg_weight

    def get_name(self) -> str:
        """Геттер названия животного.

        Returns:
            __name: название животного.
        """

        return self.__name

    def get_animal_class(self) -> str:
        """Геттер класса животного.

        Returns:
            __animal_class: класс животного.
        """

        return self.__animal_class

    def get_avg_weight(self) -> int:
        """Геттер среднего веса животного.

        Returns:
            __avg_weight: средний вес животного.
        """

        return self.__avg_weight

    def set_name(self,name) -> None:
        """Сеттер названия животного.

        Args:
            name: название животного.
        """

        if name!='':
            self.__name=name

    def set_animal_class(self,animal_class) -> None:
        """Сеттер класса животного.

        Args:
            animal_class: класс животного.
        """

        if animal_class!='':
            self.__animal_class=animal_class

    def set_avg_weight(self,avg_weight) -> None:
        """Сеттер среднего веса животного.

        Args:
            avg_weight: средний вес животного.
        """

        if avg_weight>0:
            self.__avg_weight=avg_weight

    def show(self) -> str:
        """Вывод полной информации о животном."""

        print(
            f'Название: {self.__name}\n'
            f'Класс: {self.__animal_class}\n'
            f'Средний вес: {self.__avg_weight} кг'
        )

    def get_type(self):
        """Получение весовой категории животного.

        Returns:
            'Легкий вес': текущее животное легкое.
            'Средний вес': текущее животное среднее по весу.
            'Тяжелый вес': текущее животное тяжелое.
        """

        if self.__avg_weight < 25:
            return 'Легкий вес'
        elif self.__avg_weight < 60:
            return 'Средний вес'
        else:
            return 'Тяжелый вес'

    def compare_animal_weight(self, animal):
        """Сравнение весов животных.

        Returns:
            'легче': первое животное легче второго.
            'тяжелее': первое животное тяжелее второго.
            'равны': вес первого животного равен весу второго.
        """

        if self.__avg_weight < animal.get_avg_weight():
            return 'легче'
        elif self.__avg_weight > animal.get_avg_weight():
            return 'тяжелее'
        else:
            return 'равен'

class Menu:
    """
    Класс меню для работы с животными.
    """


    def __init__(self, first_animal, second_animal):
        """Конструктор класса.

        :param first_animal: первое животное.
        :param second_animal: второе животное.
        """

        self.__first_animal=first_animal
        self.__second_animal=second_animal

    def show_menu(self) -> None:
        """Показ возможных действий."""

        print(
            '\n..::МЕНЮ ВЗАИМОДЕЙСТВИЯ С ЖИВОТНЫМИ::..\n'
            '1 - Создать первое животное\n' 
            '2 - Изменить первое животное\n'
            '3 - Изменить второе животное\n'
            '4 - Проверить к какой весовой категории относится животное\n'
            '5 - Сравнить вес двух животных\n'
            '6 - Показать информацию о животных\n'
            '7 - Выход\n'
        )

    def user_choice(self, choice) -> int:
        """Выбор пользователя и соответственно действия в зависимости от выбора.

        Args:
            choice: выбор пользователя.
        """

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

    def create_animal(self, animal) -> None:
        """
        Создаем животное, используя полученные данные.
        """

        name = str(input('\nВведите название животного: '))
        animal_class = str(input('Введите класс животного: '))
        avg_weight = int(input('Введите средний вес животного: '))

        animal.set_name(name)
        animal.set_animal_class(animal_class)
        animal.set_avg_weight(avg_weight)

    def change_animal(self, animal) -> None:
        """
        Меняем параметры животного, используя полученные данные.
        """

        print(
            '\nЧто хотите изменить?\n'
            '1 - Название\n'
            '2 - Класс\n'
            '3 - Средний вес\n'
        )

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
        """
        Вывод весовой категории животного.
        """

        print(f"\nПервое животное: {self.__first_animal.get_type()}")

        print(f"Второе животное: {self.__second_animal.get_type()}")

    def show_animals(self):
        """
        Показ животных.
        """

        print('\nПервое животное:')

        self.__first_animal.show()

        print('\nВторое животное: ')

        self.__second_animal.show()

    def compare_animal_weights(self):
        """
        Вывод сравнения животных.
        """
        answer = self.__first_animal.compare_animal_weight(self.__second_animal)

        print(f'\nВес первого животного {answer} второго')


class Main:
    """Основной класс программы."""


    def run(self):
        """Приводим программу к работе."""

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