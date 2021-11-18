class Algorithm:
    def __init__(self, num_1, result):
        self.num_1 = num_1
        self.result = result

    def sum_number(self):
       numbers = [2, 7, 11, 15]
       desired_sum = 9
       for i in numbers:
           for a in numbers:
               if i + a == desired_sum:
                   # return print(i, a)
                    print([numbers.index(i), numbers.index(a)])

    def __str__(self):
        return f'Name: {self.num_1}\n' \
               f'Result: {self.result}'


algorithm = Algorithm(num_1= '2, 7', result='9')
print(algorithm)
algorithm.sum_number()
