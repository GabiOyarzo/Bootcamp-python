from Mascota import Mascota  # Importar solo la clase Mascota

class Ninja:
    cantidad = 20

    def __init__(self, nombre, apellido, premios, comida_mascota, mascota):
        self.nombre = nombre
        self.apellido = apellido
        self.premios = premios
        self.comida_mascota = comida_mascota
        self.mascota = mascota

    def caminar(self):
        self.mascota.jugar(self)  # Pasar la instancia de ninja como argumento
        return self

    def alimentar(self, cantidad1):
        if cantidad1 > self.cantidad:
            print(f"No queda comida para {self.nombre}")
        else:
            self.mascota.comer(cantidad1, self)  # Pasar la instancia de ninja como argumento
            self.cantidad -= cantidad1
            self.comida_mascota -= cantidad1
        return self

    def bañar(self):
        self.mascota.ruido()
        return self


ninja = Ninja("Gabriela", "Oyarzo", "galletas", 20, Mascota("Lin", "perro", "premios"))
Lin = Mascota("Lin", "perro", "premios")
ninja.alimentar(10).bañar().caminar()
Lin.dormir(ninja)  # Pasar la instancia de ninja como argumento
