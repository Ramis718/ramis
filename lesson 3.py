class Tarif:
    def __init__(self, number, name, summary):
        self.number = number
        self.name = name
        self.summary = summary


    def call(self):
        return f'This number:{self.number}, can call but with restriction'


    def __str__(self):
        return f'Name:{self.name}\n'\
                f'Number:{self.number}\n' \
                f'Summery:{self.summary}'

number_1 = Tarif(name='Ramis',
                 number='0999413841',
                 summary='280')
print(number_1)
print('-----------------------------------------------------')


class UnlCallTarif(Tarif):
    def unl_call(self):
        return f'This number:{self.number}, can call but without restriction'

    def __str__(self):
        return super(UnlCallTarif, self).__str__()


number_2 = UnlCallTarif(name='Adi',
                        number='0708097865',
                        summary='2000')
print(number_2)
print('-----------------------------------------------------')

class UnlInternetTarif(Tarif):
   def unl_internet(self):
        return f'Your Internet package is unlimited'

   def __str__(self):
        return super(UnlInternetTarif, self).__str__() 

number_3 = UnlInternetTarif(name='Nurik',
                            number='0999999999',
                            summary='5000')
print(number_3)


class DiamondTarif(UnlInternetTarif, UnlCallTarif):
    def __str__(self):
        return super(DiamondTarif, self).__str__()

diamond = DiamondTarif(name='Aza',
                       number='0666666666',
                       summary=10000)
print(diamond.unl_call())
print(diamond.unl_internet())
print(diamond.call())
print(diamond)


