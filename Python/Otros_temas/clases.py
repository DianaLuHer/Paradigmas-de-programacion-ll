class Person:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludo(self):
        print(f"H {self.nombre} and I am {self.edad} years old.")


person = Person("Diana", 23)
person.saludo()