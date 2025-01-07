# class PrivateExample:
#     def __init__(self, value):
#         self.__value = value

#     def __info(self):
#         return self.__value
    
# private = PrivateExample('private')
# print(private.__info())
# print(private.__value)

import datetime

class Car:
    def __init__(self, mark, model, year, mileage):
        self.mark = mark
        self.model = model
        self._year = year
        self.__mileage = mileage

    def info(self):
        return f'Марка машины - {self.mark}\nМодель - {self.model}'
    
    def _calculate_age(self):
        current = datetime.datetime.now().year
        return f'Возраст машины - {current - self._year}'
    
    def __update_mileage(self, mileage_update = 1000):
        self.__mileage = mileage_update
        return self.__mileage
    
    def set_mileage(self):
        return self.__update_mileage()
    
car = Car('Mazda', 'RX8', 2011, 140000)
print(car.info())
print(car._calculate_age())
print(car.set_mileage())