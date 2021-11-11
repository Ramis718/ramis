import random

class TimeDesk:
    def __init__(self, seconds):
        self.seconds = seconds

    def time_2(self):
        min = self.seconds // 60
        self.seconds -= 60*min

        hours = self.seconds // 3600
        self.seconds -= 3600*hours

        day = self.seconds // 86400
        self.seconds -= 86400*day

        general_resultat = (f'day: {day}, hours: {hours} min: {min}, seconds: {self.seconds}')
        return general_resultat


# time_1 = TimeDesk(80)
# print(time_1.time_2())




class Car:
    def __init__(self, name, color):
        self.name = name
        self.color = color


    @property
    def overview(self):
         car = self.name + ' ' + self.color
         return car


    @overview.setter
    def overview(self, car):
        self.name, self.color = car.split()


    @overview.deleter
    def overview(self):
        self.name =None
        print('Name delete')

    def __str__(self):
        return f'Car: {self.name}  {self.color}'

    @staticmethod
    def is_adult(age):
        if age > 18:
            return True
        else:
            return False



car_1 = Car(name='BMW', color='black')
print(car_1)
print(car_1.overview)

car_1.name = 'Mersedes'
print(car_1.overview)

del car_1.overview
print(car_1.overview)

print(car_1.is_adult(94))

