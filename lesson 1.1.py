class Car:
    def __init__(self, brand, color, type_car, amount_passenger, max_speed,
                 engine, country, year, mechanic):
        if isinstance(brand, str):
            self.brand = brand
        else:
            raise ValueError('Brand should be string')
        if isinstance(color, str):
            self.color = color
        else:
            raise ValueError('Color should be string')
        if isinstance(type_car, str):
            self.type_car = type_car
        else:
            raise ValueError('Type Car should be string')
        if isinstance(amount_passenger, int):
            self.amount = amount_passenger
        else:
            raise ValueError('Amount passenger should be integer')
        if isinstance(max_speed, int):
            self.max_speed =max_speed
        else:
            raise ValueError('Max speed should be string')
        if isinstance(engine, float):
            self.engine =engine
        else:
            raise ValueError('Engine should be float')
        if isinstance(country, str):
            self.country =country
        else:
            raise ValueError('Countru should be string')
        if isinstance(year, int):
           self.year = year
        else:
            raise ValueError('Year should be integer')
        if isinstance(mechanic, str):
            self.mechanic = mechanic
        else:
            raise ValueError('Mechanic should be string')


    def tunning(self, cost):
        car_cost = 1000
        summary = car_cost + cost
        return summary
    def __str__(self):
        return f'BRAND: {self.brand}\n'\
               f'Color: {self.color}\n'\
               f'Year: {self.year}\n'\
               f'Country: {self.country}\n'\
               f'Amount: {self.amount}\n'\
               f'Max speed: {self.max_speed}\n'\
               f'Type car: {self.type_car}\n'\
               f'Mechanic: {self.mechanic}\n'\
               f'Engine: {self.engine}'

car_1 = Car(brand='BMW', color='red', year=2021, country='Germaby', amount_passenger=4,
            max_speed=350, type_car='Crossover', mechanic='Nope', engine=5.5)

print(car_1)
print(car_1.tunning(80))

