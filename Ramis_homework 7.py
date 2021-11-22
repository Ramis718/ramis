class Algorithm:
    def __init__(self):
        self.my_list = [5, 1, 30, 10, 20,1,5,6,4,2,89,2,9,2,7,21,67,2,36,132,37,3,56,4]


    def bubble_sort(self):

        swapped = False

        for x in range(len(self.my_list) -1, 0, -1):
             for y in range(x):
                 if self.my_list[y] > self.my_list[y + 1]:
                     self.my_list[y], self.my_list[y + 1] = self.my_list[y + 1], self.my_list[y]
                     swapped = True
             if swapped:
                swapped = False

             else:
                break

        return  self.my_list

    def porteshin(self, lst):
        if len(lst) <= 1:
            return lst
        else:
            g = lst[0]
            left = list(filter(lambda x: x < g, lst))
            center = [x for x in self.my_list if x == g]
            right = list(filter(lambda x: x > g, lst))
            return self.porteshin(left) + center + self.porteshin(right)

    def quick_sort(self):

        if len(self.my_list) <= 1:
            return self.my_list
        else:
            g = self.my_list[0]
            left = list(filter(lambda x: x < g, self.my_list))
            center = [x for x in self.my_list if x == g]
            right = list(filter(lambda x: x > g, self.my_list))
            return self.porteshin(left) + center + self.porteshin(right)


h = Algorithm()
print(h.bubble_sort())
print(h.quick_sort())



class Light:
    def __init__(self):
        self.number = 3443

    def palindrome_str(self):
     if self.number < 0:
            return False
     n = 1
     for i in range(len(str(self.number))):
        if str(self.number)[i] != str(self.number)[len(str(self.number)) - n]:
            return False
        n += 1
        return True


a = Light()
print(a.palindrome_str())

