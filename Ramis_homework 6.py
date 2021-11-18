class Algorithm:
   def sum_number(self):
       numbers = [2, 7, 11, 15]
       desired_sum = 9
       for i in numbers:
           for a in numbers:
               if i + a == desired_sum:
                   # return print(i, a)
                    print([numbers.index(i), numbers.index(a)])





algorithm = Algorithm()
algorithm.sum_number()
