class Panda:
    def __init__(self, name, weight, color, fur):
        self.name = name
        self.weight = weight
        self.color = color
        self.fur = fur

    def style_kung_fu(self):
        style = f'Dragon Warrior, cause I\'m {self.name}'
        return style

    def __str__(self):
        return f'Name: {self.name}\n' \
               f'Weight: {self.weight}\n' \
               f'Color: {self.color}\n' \
               f'Fur: {self.fur}'


panda = Panda(name='Po', weight=300, color='Black and White', fur=True)
print(panda)
print(panda.style_kung_fu())


class Tiger:
    def __init__(self, name, weight, color, fur):
        self.name = name
        self.weight = weight
        self.color = color
        self.fur = fur

    def style_kung_fu(self):
        style = f'\nTiger style, cause I\'m {self.name}'
        return style

    def __str__(self):
        return f'\nName: {self.name}\n' \
               f'Weight: {self.weight}\n' \
               f'Color: {self.color}\n' \
               f'Fur: {self.fur}\n'


tiger_1 = Tiger(name='Òigrisa',
                weight=100,
                color='B polosky',
                fur=True)

print(tiger_1.style_kung_fu())
print(tiger_1)
