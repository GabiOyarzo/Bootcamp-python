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
barbara = Usuario('Bárbara')
emilio = Usuario('Emilio')

gabriela.hacer_deposito(200)
gabriela.hacer_deposito(90)
gabriela.hacer_deposito(80)
gabriela.hacer_retiro(300)
gabriela.mostrar_balance_usuario()
barbara.hacer_deposito(300)
barbara.hacer_deposito(20)
barbara.hacer_retiro(30)
barbara.hacer_retiro(100)
barbara.mostrar_balance_usuario()
emilio.hacer_deposito(400)
emilio.hacer_retiro(20)
emilio.hacer_retiro(40)
emilio.hacer_retiro(100)
gabriela.transfer_dinero(emilio,150)
gabriela.mostrar_balance_usuario()
emilio.mostrar_balance_usuario()