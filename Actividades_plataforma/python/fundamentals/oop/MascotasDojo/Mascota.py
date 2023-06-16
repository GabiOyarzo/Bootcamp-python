class Mascota:
    def __init__(self, name, tipo, golosinas):
        self.name = name
        self.tipo = tipo
        self.golosinas = golosinas
        self.energia = 20
        self.salud = 20

    def dormir(self, ninja):
        self.energia += 25
        print(f"{self.name} se ha dormido en la cama de {ninja.nombre}")
        return self

    def comer(self, cantidad, ninja):
        self.energia += 5
        self.salud += 10
        print(f"{self.name} se encuentra comiendo {ninja.comida_mascota} que le dio {ninja.nombre}")
        return self

    def jugar(self, ninja):
        self.salud += 5
        print(f"{self.name} está feliz por jugar con {ninja.nombre} y {ninja.nombre} le dio {self.golosinas}")
        return self

    def ruido(self):
        print(f"{self.name} ha producido un ruido")
