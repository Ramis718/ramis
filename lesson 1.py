class Human:
    def __init__(self, name, age, height, gender):
        self.myname = name
        self.age = age
        self.height = height
        self.gender = gender

    def __str__(self):
        return f'Name: {self.myname}\n' \
               f'Age: {self.age}\n' \
               f'Height: {self.height}\n' \
               f'Gender: {self.gender}\n'

    def can_calculate(self, number_1, number_2):
        summer = number_1 + number_2
        return summer

    def can_say_hello(self):
        return 'Hello world'

class Programmer(Human):
    def __init__(self, name, age, height, gender, language, fas_tuping, logic_thinking, ):
        super().__init__(name,age, height, gender)
        self.language = language
        self.fast = fas_tuping
        self.logic = logic_thinking

    def can_feeely_use_laptop(self):
        print('Yeap, I can freely use laptop like a God')

    def __str__(self):
        return f'Languages: {self.language}\n' \
               f'Fast Typing: {self.fast}\n' \
               f'Logic: {self.logic}'



human_1 = Human(name='Ramis', age= 19, height=178, gender='male')
human_2 = Human('Aza', 20, 180, 'famale')
# print(human_1.can_calculate(int(input("number_1:")), int(input('number_2:'))))
# print(human_1)
# print(human_2)
# print(human_1.can_say_hello())
proger = Programmer(language='Python',
                    fas_tuping=True, logic_thinking=True,
                    name='Ramis', age= 19, height=178,
                    gender='male')
print(proger)

