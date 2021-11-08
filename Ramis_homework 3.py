class Nokia:
    def __init__(self, model, design, volume, color):
        self.model = model
        self.design = design
        self.volume = volume
        self.color = color


    def known(self):
        return f'This known {self.model}'

    def popular(self):
        return f'This {self.design} popular'

    def __str__(self):
        return f'Model:{self.model}\n' \
               f'Design:{self.design}\n' \
               f'Volume:{self.volume}\n' \
               f'Color:{self.color}\n'

nokia_1 = Nokia(model='3110', design ='button', volume='2', color='blue and white')
print(nokia_1)
print('-----------------------------------------------')


class Sumsung(Nokia):

    def not_popular(self):
        return f'This {self.model} not popular'

    def like(self):
        return f'This {self.design} everyone likes'

    def __str__(self):
        return super(Sumsung, self).__str__()

sumsung_1 = Sumsung(model='s8', design='sensory', volume='4', color='black')
print(sumsung_1)
print('-----------------------------------------------')

class Gresso(Nokia):
    def like_color(self):
        return f'This {self.color} everyone like'

    def used(self):
        return f'This {self.model} used'

    def __str__(self):
        return super(Gresso, self).__str__()

gresso_1 = Gresso(model='Meridian M4', design='button', volume='32', color='black titanium')
print(gresso_1)
print('-----------------------------------------------')

class Apple(Sumsung, Gresso):
    def peace(self):
        return f'This {self.model} popular in peace'

    def design_a(self):
        return f'This {self.design} the first'

    def __str__(self):
        return super(Gresso, self).__str__()

apple_1 = Apple(model='Alpha', design='frameless', volume='128', color='gold')
print(apple_1)
print(apple_1.peace())
print(apple_1.design_a())
print(apple_1.used())
print(apple_1.like_color())
print(apple_1.like())
print(apple_1.not_popular())
print(apple_1.known())
print(apple_1.popular())
print('****************************************************')

class Flowers:
    def __init__(self, name, age, color, height):
        self.name = name
        self.age = age
        self.color = color
        self.height = height


    def like_d(self):
        return f'Flowers called: {self.name}'

    def cool(self):
        return f'like {self.color}'
    def __str__(self):
        return f'Name:{self.name}\n' \
               f'Age:{self.age}\n' \
               f'Color:{self.color}\n' \
               f'Height:{self.height}'

roza_1 = Flowers(name='Rose', age='1', color='red', height='90')
print(roza_1)

class Flowers_1(Flowers):
    def __str__(self):
        return super(Flowers_1, self).__str__()

    def love(self):
        return f'This love {self.name} warm time'

    def people(self):
        return f'People like this flowers'

romashca_1 = Flowers_1(name='chamomile', age='2', color='white', height='12')
print(romashca_1)

class Flowers_2(Flowers):
    def __str__(self):
        return super(Flowers_2, self).__str__()

    def cute(self):
        return f'People think these flowers are cute'

    def smell_1(self):
        return f'Recognizable smell'

gvozdiki_1 = Flowers_2(name='carnation', age='1.5', color='red', height='30')
print(gresso_1)


class Flowers_3(Flowers):
    def __str__(self):
        return super(Flowers_3, self).__str__()

    def not_like(self):
        return f"Don't like these flowers"
    def bad(self):
        return f'This flowers bad'

fic_1 = Flowers_3(name='ficus', age='2', color='green', height='20')
print(fic_1)
print(fic_1.bad())
print(fic_1.not_like())
print(fic_1.cool())
print(fic_1.like_d())
print('****************************************')



