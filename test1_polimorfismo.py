#Aulas de Polimorfismo de - M.A:

class Animal: # Fixed typo here
    def emitir_som(self):
      pass

class Cachorro(Animal):
    def emitir_som(self):
      print("Au Au")

class Gato(Animal):
    def emitir_som(self):
      print("Miau")

cachorro = Cachorro()
gato = Gato()

animal = [cachorro, gato]

for animal in animal:
  animal.emitir_som()