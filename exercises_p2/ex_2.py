# 2. Crie funções para um banco. a classe conta possui atributos privados para o saldo do usuário. crie as funções de depósito e saque.

class Account:
    def __init__(self, initial_balance):
        self.__balance = float(initial_balance)


    def withdraw(self, amount):
        self.__balance = self.__balance - amount
        print(self.__balance)


    def deposit(self, amount):
        self.__balance = self.__balance + amount
        print(self.__balance)


    def show_balance(self):
        print(self.__balance)
