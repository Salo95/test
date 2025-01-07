'''ООП - Объектно Ориентированное Программа'''

class Car: #shablon ili chertyozh
    def __init__(self, wheel, motor, body): # __init__ - constructor
        self.wheel = wheel
        self.motor = motor #self - ssylka na tekushiy obyekt
        self.body = body #otribut classa

        self.bak = 20
        self.if_start = False

    def info(self): #funktsiya vnutri classa - method
        print(f'Колесо - {self.wheel}, мотор - {self.motor}, кузов - {self.body}')

    def start(self):
        if self.bak > 0:
            self.if_start = True
            print('Машина заведена')
        else:
            print('У машины нет топлива')

    def stop(self):
        self.if_start = False
        print('Машина заглушена')

    def drive(self, city):
        if self.if_start == True:
            print(f'Машина едет в {city}')
        else:
            print('Машина не заведена')

car = Car('R20', 'V8', 'khan') #examplyar classa
car.info() #vyzov methoda, obrashayas' k examplyaru
car.start()
car.drive('Neapole')
car.stop()
