class ZOO:
    def __init__(self, name, color, height, gender, weight):
        if isinstance(name, str):
            self.name = name
        else:
            raise ValueError('Name should be string')
        if isinstance(color, str):
            self.color = color
        else:
            raise ValueError('Color should be string')
        if isinstance(height, int):
            self.hieght = height
        else:
            raise ValueError('Height should be integer')
        if isinstance(gender, str):
           self.gender = gender
        else:
            raise ValueError('Gender should be string')
        if isinstance(weight, int):
            self.weight = weight
        else:
            raise ValueError('Weight should be integer')



    def __str__(self):
      return f' ZOO name:{self.name}\n' \
             f'Zoo color:{self.color}\n'\
             f'Zoo height:{self.hieght}\n'\
             f'Zoo gender:{self.gender}\n'\
             f'Zoo weight:{self.weight}\n'



animal_1 = ZOO(name='Horse',color='black', height=150,  gender='male', weight=400)

animal_2 = ZOO(name='Eagle',  color= 'brown', height=75, gender='male', weight=6)

animal_3 = ZOO(name='Shark',  color='blue',  height= 5, gender='male', weight=800)

# print(animal_1)
# print(animal_2)
# print(animal_3)

class Animal(ZOO):
    def __init__(self, name, color, height, gender, weight, views, age, action):
        super().__init__(name, color, height, gender, weight)
        self.action = action

        if isinstance(views, str):
            self.views = views
        else:
            raise ValueError('Views should be string')

        if isinstance(action, str):
            self.action = action
        else:
            raise ValueError('Action should be string')

        if isinstance(age, int):
            self.age = age
        else:
            raise ValueError('Age should be integer')


    def __str__(self):
        return super().__str__(),f'Animals action is {self.action}\n' \
                                  f'Animals weight is {self.action}\n'\
                                 f'Zoo age:{self.age}\n'


zoo_1 = Animal(name='Horse',views= 'Beast', color='black', age=25, height=150,
               gender='male', weight=400, action='can drees up trampolines')

zoo_2 = Animal(name='Eagle', views='Bird', color= 'brown', age=8, height=75,
               gender='male', weight=6, action='can see 3 kille')

zoo_3 = Animal(name='Shark', views='Fish', color='blue', age=25, height= 5,
               gender='male', weight=800, action='can survive in different situations')



class Zoo_show:
    def __init__(self, zoo):
        self.zoo = zoo
        self.ticket = 0

        if (zoo.name == 'Horse'):
            self.ticket = '20$'

        if (zoo.name == 'Eagle'):
            self.ticket = '30$'

        if (zoo.name == 'Shark'):
            self.ticket = '50$'

    def billet(self):
        return "Show will coast" + self.ticket

    def __str__(self):
        return f'{self.zoo.name} will show {self.zoo.action}'

show_1 = Zoo_show(zoo_1)
show_2  = Zoo_show(zoo_2)
show_3 = Zoo_show(zoo_3)
print(show_1)
print(show_1.billet())

print(show_2)
print(show_2.billet())

print(show_3)
print(show_3.billet())




