#   Actividad Usuario 
# --------------------------------------------------------

class Usuario:		
    def __init__(self, name):
        self.name = name
        self.balance_cuenta = 200
    
    def hacer_deposito(self, amount):
        self.balance_cuenta += amount
        print(f"Se ha depositado ${amount} en la cuenta de {self.name}")

    def hacer_retiro(self, amount):
        self.balance_cuenta -= amount
        print(f"Se ha retirado ${amount} en la cuenta de {self.name}")

    def mostrar_balance_usuario(self):
        print(f"La cuenta de {self.name} tiene: ${self.balance_cuenta}")

    def transfer_dinero(self, other_user, amount):
        print(f"{self.name} ha transferido ${amount} en la cuenta de {(other_user.name)}" )
        self.balance_cuenta -= amount
        other_user.balance_cuenta += amount
    # Agregando : transferencia

gabriela = Usuario('Gabriela')
emilio = Usuario('Emilio')
barbara = Usuario('Bárbara')

gabriela.hacer_deposito(200)
gabriela.mostrar_balance_usuario()
gabriela.transfer_dinero(emilio,150)
barbara.mostrar_balance_usuario()
emilio.mostrar_balance_usuario()