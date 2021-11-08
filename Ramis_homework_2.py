class Dad:
    def __init__(self, name, age, height, health, vision):
        self.name = name
        self.age = age
        self.height = height
        self.health = health
        self.vision = vision

    def health_health(self):
        return f'I have health {self.health}'

    def __str__(self):
        return f'Name:{self.name}\n' \
               f'Age:{self.age}\n' \
               f'Height:{self.height}\n' \
               f'Health:{self.health}\n' \
               f'Vision:{self.vision}'

dad_1 = Dad(name='Victor',
            age=80,
            height=158,
            health=False,
            vision=False)
print(dad_1)
print(dad_1.health_health())
print('________________________________________')

class Father(Dad):
    def __init__(self, name, age, height, health, vision, work, money):
        super().__init__(name, age, height, health, vision)
        self.work = work
        self.money = money

    def money_money(self):
        return f'I have {self.money} money'

    def __str__(self):
        return super(Father, self).__str__() + f'\nWork:{self.work}\n' \
                                          f'Money:{self.money}'\

father_1 = Father(name='Oleg',
            age=30,
            height=180,
            health=True,
            vision=True, work=True, money=10000)

print(father_1)
print(father_1.money_money())
print('________________________________________')

class Child(Father):
    def __init__(self, name, age, height, health, vision, work, money, school, language):
        super().__init__(name, age, height, health, vision, work, money)
        self.school = school
        self.language = language

    def say_which_language(self):
        return f'Im using {self.language}'

    def __str__(self):
        return super(Child, self).__str__() + f'\nSchool:{self.school}\n' \
                                              f'Language:{self.language}'

child_1 = Child(name='Serega',
            age=18,
            height=175,
            health=True,
            vision=False, work=False, money=True, school=True, language='English')
print(child_1)
print(child_1.say_which_language())
print('************************************************** ')


class SomeClass:
    def _internal(self):
      print('This is an internal method')
    def __protected(self):
         print('This is an protected method')

    def __init__(self, home, dacha):
        self._internal_obj = home
        self.__protected_obj = dacha

a = SomeClass(home=300, dacha= 1000)
a._internal()
# a.__protected()
print('*********************************************')

class Usa:
    def attack(self, h):
        print('bomb attack')
class Russia:
    def attack(self):
        print('attack with vodka')
class China:
    def attack(self):
        print('beetle attack')

us = Usa()
us.attack()

ru = Russia()
ru.attack()

ch = China()
ch.attack()



# def intro(weapons):
#     weapons.attack()
#
#
# usa = Usa()
# intro(usa)
# russia = Russia()
# intro(russia)
# china = China()
# intro(china)
print('*********************************')

class Dad:
    def day(self):
        print('Grandfather spends most of the day at home')

class Father(Dad):
    def day(self):
        print('Father spends most of the day at work')

class Child(Father):
    def day(self):
        print('The child spends most of the day at school')

def intro(home):
    home.day()

dad = Dad()
intro(dad)
father = Father()
intro(father)
child = Child()
intro(child)
