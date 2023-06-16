class Ninja:
    cantidad = 20

    def __init__(self, nombre, apellido, premios, comida_mascota, mascota):
        self.nombre = nombre
        self.apellido = apellido
        self.premios = premios
        self.comida_mascota = comida_mascota
        self.mascota = mascota

    def caminar(self):
        self.mascota.jugar()
        return self

    def alimentar(self, cantidad1):
        if cantidad1 > self.cantidad:
            print(f"No queda comida para {self.nombre}")
        else:
            self.mascota.comer(cantidad1)
            self.cantidad -= cantidad1
        return self
    def bañar(self):
        self.mascota.ruido()
        return self

class Mascota:
    def __init__(self, name, tipo, golosinas):
        self.name = name
        self.tipo = tipo
        self.golosinas = golosinas
        self.energia = 20
        self.salud = 20

    def dormir(self):
        self.energia += 25
        print(f"{self.name} se ha dormido en la cama de {ninja.nombre}")
        return self

    def comer(self, cantidad):
        self.energia += 5
        self.salud += 10
        print(f"{self.name} se encuentra comiendo {ninja.comida_mascota} que le dio {ninja.nombre}")
        return self

    def jugar(self):
        self.salud += 5
        print(f"{self.name} está feliz por jugar con {ninja.nombre} y {ninja.nombre} le dio {self.golosinas}")
        return self

    def ruido(self):
        print(f"{self.name} ha producido un ruido")

ninja = Ninja("Gabriela", "Oyarzo", "galletas", "croquetas", Mascota("Lin", "perro", "premios"))
Lin = Mascota("Lin", "perro", "premios")
ninja.alimentar(10).bañar().caminar()
Lin.dormir()
