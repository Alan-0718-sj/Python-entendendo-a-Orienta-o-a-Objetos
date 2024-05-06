# from cliente import Cliente
# cliente = Cliente("Pedro")
#  import os
#  os.system("cls")

class Cliente:

    def pen(self, msg):
        tam = len(msg)
        print('01' * tam)
        print(f'  {msg}')
        print('01' * tam)

    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        # self.pen(msg):
        print("chamando @property nome()")
        return self.__nome.title()
    
    @nome.setter
    def nome(self, nome):
        print("chamando setter nome()")
        self.__nome = nome
