class Wizard:
    def __init__(self, first, last):
        self.first = first
        self.last = last


    def emaling(self):
        email = f'{self.first}.{self.last}@gmail.com'
        return email

    @staticmethod
    def add_some():
        summery = 1 + 2
        return summery

    @property
    def fullname(self):
        name = self.first + ' ' + self.last
        return name

    @fullname.setter
    def fullname(self, name):
        self.first, self.last = name.split()

    @fullname.deleter
    def fullname(self):
        self.first = None
        self.last = None
        print('Fullname deleted')

    def __str__(self):
        return f'Fullname: {self.first}  {self.last}'

wiz_1 = Wizard(first='Liz',  last='Wkadkj')

print(wiz_1)
print(wiz_1.fullname)
print(wiz_1.emaling())
wiz_1.first = "ghhgh"
print(wiz_1.fullname)
del wiz_1.fullname
print(wiz_1.fullname)
