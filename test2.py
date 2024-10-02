# Polimorfismo, exemplo de veículos:

class Veiculo:
  def tipo_de_veiculo(self):
    pass

class Carro(Veiculo):
  def tipo_de_veiculo(self):
    print("Vrummmmmmmmmmm")

class Moto(Veiculo):
  def tipo_de_veiculo(self):
    print("DanDanDan Dannnnn")

carro = Carro()
moto = Moto()

veiculo = [carro, moto]

for veiculo in veiculo:
  veiculo.tipo_de_veiculo()