# name = ('Asko', 'Isko', 'Sema')
# name = list(name)
# name.append('Aslan')
# name = tuple(name)
# print(name)

# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def eat(self):
#         print(f'{self.name} ест')

#     def sleep(self):
#         print(f'{self.name} спит')

# class Walker:
#     def __init__(self, name):
#         self.name = name

#     def eat(self):
#         print(f'{self.name} ест')

#     def sleep(self):
#         print(f'{self.name} спит')

#     def walk(self):
#         print(f'{self.name} ходит')

# class Swimmer:
#     def __init__(self, name):
#         self.name = name

#     def eat(self):
#         print(f'{self.name} ест')

#     def sleep(self):
#         print(f'{self.name} спит')

#     def swim(self):
#         print(f'{self.name} плавает')

# class Flyer:
#     def __init__(self, name):
#         self.name = name

#     def eat(self):
#         print(f'{self.name} ест')

#     def sleep(self):
#         print(f'{self.name} спит')

#     def fly(self):
#         print(f'{self.name} летает')

# class Penguin(Animal, Walker, Swimmer):
#     def __init__(self, name):
#         super().__init__(name)

#     def eat(self):
#         return super().eat()
    
#     def sleep(self):
#         return super().sleep()
    
#     def walk(self):
#         return super().walk()
    
#     def swim(self):
#         return super().swim()

#     def describe(self):
#         print(f'{self.name} может ходить и плавать')

# class Duck(Animal, Walker, Swimmer, Flyer):
#     def __init__(self, name):
#         super().__init__(name)

#     def eat(self):
#         return super().eat()
    
#     def sleep(self):
#         return super().sleep()
    
#     def walk(self):
#         return super().walk()
    
#     def swim(self):
#         return super().swim()
    
#     def fly(self):
#         return super().fly()
    
#     def describe(self):
#         print(f'{self.name} может ходить, плавать и летать')

# class Bat(Animal, Flyer):
#     def __init__(self, name):
#         super().__init__(name)

#     def eat(self):
#         return super().eat()
    
#     def sleep(self):
#         return super().sleep()
    
#     def walk(self):
#         return super().walk()
    
#     def fly(self):
#         return super().fly()
    
#     def describe(self):
#         print(f'{self.name} может летать')
# panda = Animal('Панда')
# panda.eat()
# panda.sleep()

# dog = Walker('Собака')
# dog.sleep()
# dog.walk()

# shark = Swimmer('Акула')
# shark.eat()
# shark.swim()

# eagle = Flyer('Орёл')
# eagle.fly()

# penguin = Penguin('Пингвин')
# penguin.swim()
# penguin.describe()

# duck = Duck('Утка')
# duck.walk()
# duck.describe()

# bat = Bat('Летучая мышь')
# bat.fly()
# bat.describe()

class Employee:
    def __init__(self, name, rate):
        self.name = name
        self.rate = rate

    def calculate_salary(self):
        return 0
    
    def display_info(self):
        return f'Имя - {self.name}'

class FullTimeEmployee(Employee):
    def __init__(self, name, rate):
        super().__init__(name, rate)

    


        