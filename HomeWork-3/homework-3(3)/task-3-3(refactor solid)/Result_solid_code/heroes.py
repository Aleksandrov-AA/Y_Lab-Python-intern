from antagonistfinder import AntagonistFinder
from typing import Generator, List, Tuple


class SuperHero:

    def __init__(self, name, can_use_ultimate_attack = True):
        self.name = name
        self.can_use_ultimate_attack = can_use_ultimate_attack
        self.finder = AntagonistFinder()

    def find(self, place):
        self.finder.get_antagonist(place)

    # Проблема: Герой не должен заниматься оповещениями о своей победе, это задача масс-медиа.
    # Несоблюден: Принцип единой ответственности.
    # По SOLID: Вынести оповещение в отдельный класс, занимающийся выводом информации.
    # Когда возникнут трудности? Добавьте оповещение о победе героя через газеты или через TV (на выбор)
    # а также попробуйте оповестить планеты (у которых вместа атрибута name:str используется coordinates:List[float]).
    
    # Проблема: Для каждого супергероя реализованы все методы обращения с оружием.
    # Несоблюден: Принцип разделения интерфейса
    # По SOLID: Создать классы-миксины для каждого оружия
    # Когда возникнут трудности? Попробуйте запретить Чаку норрису пользоваться лазерами из глаз!
    def fire_a_gun(self):
        print('PIU PIU')

    def incinerate_with_lasers(self):
        print('Wzzzuuuup!')

    def roundhouse_kick(self):
        print('Bump')

    def attack(self):
        self.fire_a_gun()

    # Проблема: У разных супергероев разные суперспособности
    # Несоблюден: Принцип открытости/закрытости
    # По SOLID: Каждого супергероя реализовать как наследника SuperHero и вместо изменения базового класса переопределять нужные методы
    # Когда возникнут трудности? Когда в вашем коде поселится вся команда Мстителей
    def ultimate(self):
        if self.name == 'Clark Kent':
            self.incinerate_with_lasers()

class Fire_a_gun:

    def attack(self):
        print('PIU PIU')

class Incinerate_with_lasers:

    def attack(self):
        print('Wzzzuuuup!')

class Roundhouse_kick:

    def attack(self):
        print('Bump')

class Mass_media:

    @staticmethod
    def create_news(place, hero, tv_on=False):
        place_name = getattr(place, 'coordinates', True) if getattr(place, 'coordinates', True) != True \
            else getattr(place, 'name', 'place')
        hero_name = getattr(hero, 'name', 'hero')
        tv = ' watch TV!' if tv_on == True else ' read newspaper!'
        print(f'{hero_name} saved the {place_name}!{tv}')

class Superman(SuperHero):

    def __init__(self):
        super(Superman, self).__init__('Clark Kent', True)

    # Проблема: Сигнатура метода изменилась. Если мэр города обратится к супермену как к супергерою у Кларка возникнут проблемы с атакой
    # Несоблюден: Принцип подстановки Барбары Лисков
    # По SOLID: Не допускать таких вольностей
    # Когда возникнут трудности? При первой же битве
    
class ChackNorris(Fire_a_gun, SuperHero):
    def __init__(self):
        super(ChackNorris, self).__init__('Chack Norris', False)