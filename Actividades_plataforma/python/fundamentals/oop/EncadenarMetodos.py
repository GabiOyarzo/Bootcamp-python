#   Actividad Usuario 
# --------------------------------------------------------

class Usuario:		
    def __init__(self, name):
        self.name = name
        self.balance_cuenta = 200
    
    def hacer_deposito(self, amount):
        self.balance_cuenta += amount
        print(f"Se ha depositado ${amount} en la cuenta de {self.name}")
        return self

    def hacer_retiro(self, amount):
        self.balance_cuenta -= amount
        print(f"Se ha retirado ${amount} en la cuenta de {self.name}")
        return self

    def mostrar_balance_usuario(self):
        print(f"La cuenta de {self.name} tiene: ${self.balance_cuenta}")
        return self

    def transfer_dinero(self, other_user, amount):
        print(f"{self.name} ha transferido ${amount} en la cuenta de {(other_user.name)}" )
        self.balance_cuenta -= amount
        other_user.balance_cuenta += amount
        return self
    # Agregando : transferencia

gabriela = Usuario('Gabriela')
barbara = Usuario('Bárbara')
emilio = Usuario('Emilio')

gabriela.hacer_deposito(200).hacer_deposito(90).hacer_deposito(80).hacer_retiro(300).mostrar_balance_usuario()
barbara.hacer_deposito(300).hacer_deposito(20).hacer_retiro(30).hacer_retiro(100).mostrar_balance_usuario()
emilio.hacer_deposito(400).hacer_retiro(20).hacer_retiro(40).hacer_retiro(100)
gabriela.transfer_dinero(emilio,150).mostrar_balance_usuario()
emilio.mostrar_balance_usuario()