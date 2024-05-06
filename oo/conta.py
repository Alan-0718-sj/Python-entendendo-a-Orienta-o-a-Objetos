""" Acessar Conta 
# from conta import Conta
# conta = Conta(123, "Nan", 55.5, 1000.0)
# conta2 = Conta(321, "Pedro", 100.0, 2000.0)
# conta.extrato()
# conta.deposita(15.0)
# conta.saca(15.0) """ 
""" Limpar console
import os
os.sytem("cls")

**********************************************************************
from conta import Conta                
>>> conta = Conta(123, "Nan", 55.5, 1000.0)
Construindo objeto ... <conta.Conta object at 0x000001B76E67AB50>
>>> conta2 = Conta(321, "Pedro", 100.0, 2000.0)
Construindo objeto ... <conta.Conta object at 0x000001B76E976DD0>
>>> conta2.transfere(10.0, conta)
>>> conta2.extrato()
Saldo de R$ 90.0 do titular Pedro
>>> conta.extrato()  
Saldo de R$ 65.5 do titular Nan
***********************************************************************
"""

class Conta:

    def __init__(self, numero, titular, saldo, limite): # Privado __
        print("Construindo objeto ... {}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("Saldo de R$ {} do titular {}".format(self.__saldo, self.__titular))

    def deposita(self, valor):
        self.__saldo += valor

    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel_a_sacar = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel_a_sacar

    def saca(self, valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print("O valor {} passou o limite".format(self.__valor))

    # def saca(self, valor):
    #     if(valor <= (self.__saldo + self.__limite)):
    #         self.__saldo -= valor
    #     else:
    #         print("O valor {} passou o limite".format(valor))

    def transfere(self, valor, destino): # conta2.transfere(10.0, conta)
        self.saca(valor)
        destino.deposita(valor)

    @property
    def saldo(self): # get devolve
        return self.__saldo
    
    @property
    def titular(self):
        return self.__titular
    
    @property
    def limite(self):
        return self.__limite
    
    @limite.setter
    def limite(self, limite): # set altera 
        self.__limite = limite

    @staticmethod
    def codigo_banco():
        return "001"

    @staticmethod
    def codigos_bancos():
        return {'BB':'001', 'Caixa':'104', 'Bradesco':'237'}
                   
    


