class Junior:
    def __init__(self, language, soft_skills, laptop, salary):
        self.language = language
        self.soft = soft_skills
        self.laptop = laptop
        self.salary = salary

    def say_which_langufge(self):
        return f'Im using {self.language}'

    def __str__(self):
        return f"Language : {self.language}\n" \
               f"Soft-skills : {self.soft}\n" \
               f"Laptop : {self.laptop}\n" \
               f"Salary : {self.salary}"


junior_1 = Junior(language="Python",
                  soft_skills="Good Enought",
                  laptop="gaming laptop",
                  salary="300$")

print(junior_1)
print('_______________________________')
class Middle(Junior):
    def __init__(self, language, soft_skills, laptop, salary, fast_resolving, reliable):
        super().__init__(language, soft_skills, laptop, salary)
        self.fast_resolvin = fast_resolving
        self.reliable = reliable

    def __str__(self):
        return super(Middle, self).__str__()+ f'\nResolving:{self.fast_resolvin}\n'\
                                              f'Reliable:{self.reliable}'

middle_1 = Middle(language="Python, JS, PHP, Django",
                  soft_skills="Good Enought",
                  laptop="gaming laptop",
                  salary="1000$",
                  fast_resolving="Often",
                  reliable=True)
print(middle_1.say_which_langufge())
print(middle_1)

print('*********************************')
class Senior(Middle):
    def __init__(self, language, soft_skills, laptop, salary, fast_resolving, reliable, architecture, leading_skill):
        super().__init__(language, soft_skills, laptop, salary, fast_resolving, reliable)
        self.Architecture = architecture
        self.Leading_skill = leading_skill

    def __str__(self):
        return super(Senior, self).__str__() + f'\nArchitecture: {self.Architecture}\n'\
                                               f'Leading_skill: {self.Leading_skill}'

senior_1 = Senior(language="Python, JS, PHP, Django",
                  soft_skills="Good Enought",
                  laptop="gaming laptop",
                  salary="500000$",
                  fast_resolving="Often",
                  reliable=True,
                  architecture=True,
                  leading_skill= True)

print( senior_1)



