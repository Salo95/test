'ООП, Полиморфизм'

# class Cat:
#     def __init__(self, name, preference):
#         self.name = name
#         self.preference = preference

#     def info(self):
#         print(f'Привет, меня зовут {self.name}, мне {self.preference} года')

#     def sound(self):
#         print('Мяу')

# class Dog:
#     def __init__(self, name, preference):
#         self.name = name
#         self.preference = preference

#     def info(self):
#         print(f'Привет, меня зовут {self.name}, мне {self.preference} года')

#     def sound(self):
#         print('Гав')
        
class PaymentMethod:
    def pay(self, amount):
        pass

class CreditCard(PaymentMethod):
    def pay(self, amount):
        return f'Сумма {amount}, оплачивается по кредитной карте'
    
class Pay24(PaymentMethod):
    def pay(self, amount):
        return f'Сумма {amount}, оплачивается по Pay24'
    
class PayPal(PaymentMethod):
    def pay(self, amount):
        return f'Сумма {amount}, оплачивается по PayPal'
    
class BankTransfer(PaymentMethod):
    def pay(self, amount):
        return f'Сумма {amount}, оплачивается по банковскому переводу'
    
payments = [CreditCard(), Pay24(), PayPal(), BankTransfer()]

for payment in payments:
    print(payment.pay(100))