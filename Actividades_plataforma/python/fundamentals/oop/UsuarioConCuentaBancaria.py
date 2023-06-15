class CuentaBancaria:
    nombre_banco = "Banco Nook"

    def __init__(self, tasa_interés, balance, id):
        self.tasa_interés = tasa_interés
        self.balance = balance
        self.id = id

    def depósito(self, amount, id):
        self.balance += amount
        print(f"Se ha depositado ${amount} en la cuenta {id}")
        return self

    def retiro(self, amount, id):
        self.balance -= amount
        print(f"Se ha retirado ${amount} de la cuenta {id}")
        return self

    def mostrar_info_cuenta(self, id):
        print(f"La cuenta {id} tiene un saldo actual de ${self.balance}")
        return self

    def generar_interés(self, id):
        self.balance += self.balance * self.tasa_interés
        return self

# -------------------------------------------------------------------------------------------
class Usuario:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.cuentas = []

    def crear_cuenta(self, tasa_interés, balance, id):
        cuenta = CuentaBancaria(tasa_interés, balance, id)
        self.cuentas.append(cuenta)
        print(f"Se ha creado una nueva cuenta con ID: {id} para {self.name}")
        return self

    def hacer_deposito(self, id, amount):
        cuenta = self.obtener_cuenta_por_id(id)
        if cuenta:
            cuenta.depósito(amount, id)
            print(f"Se ha depositado ${amount} en la cuenta {id} de {self.name}")
        return self

    def hacer_retiro(self, id, amount):
        cuenta = self.obtener_cuenta_por_id(id)
        if cuenta:
            cuenta.retiro(amount, id)
            print(f"Se ha retirado ${amount} de la cuenta {id} de {self.name}")
        return self

    def mostrar_balance_usuario(self, id):
        cuenta = self.obtener_cuenta_por_id(id)
        if cuenta:
            cuenta.mostrar_info_cuenta(id)
        return self

    def obtener_cuenta_por_id(self, id):
        for cuenta in self.cuentas:
            if cuenta.id == id:
                return cuenta
        return None

gabriela = Usuario('Gabriela', 'gabioyarzoe@gmail.com')
gabriela.crear_cuenta(0.2, 200, 1).crear_cuenta(0.1, 100, 2)

gabriela.hacer_deposito(1, 20).hacer_retiro(1, 150).mostrar_balance_usuario(1).mostrar_balance_usuario(2).hacer_deposito(2, 50).hacer_retiro(1, 100).mostrar_balance_usuario(2)