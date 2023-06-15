class CuentaBancaria:
    nombre_banco = "Banco Nook"
    cuentas = []

    def __init__(self, name, tasa_interés, balance):
        self.name = name
        self.tasa_interés = tasa_interés
        self.balance = balance
        CuentaBancaria.cuentas.append(self)

    def depósito(self, amount):
        self.balance += amount
        print(f"Se ha depositado ${amount} en la {self.name}")
        return self

    def retiro(self, amount):
        self.balance -= amount
        print(f"Se ha retirado ${amount} de la {self.name}")
        return self

    def mostrar_info_cuenta(self):
        print(f"La {self.name} tiene un saldo actual de ${self.balance}")
        return self

    def generar_interés(self):
        self.balance += self.balance * self.tasa_interés
        return self

    @classmethod
    def imprimir_todas_las_cuentas(cls):
        for cuenta in cls.cuentas:
            cuenta.mostrar_info_cuenta()

cuenta1 = CuentaBancaria("cuenta N°1", 0.2, 200)
cuenta2 = CuentaBancaria("cuenta N°2", 0.1, 100)

cuenta1.depósito(20).depósito(10).depósito(35).retiro(100).generar_interés().mostrar_info_cuenta()
cuenta2.depósito(50).depósito(1000).retiro(100).retiro(200).retiro(20).retiro(50).generar_interés().mostrar_info_cuenta()

CuentaBancaria.imprimir_todas_las_cuentas()