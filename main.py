minutos = input("Digite um número: ")
baterias = 100
pedras = (minutos * baterias * 300) / (15 * 5)

print(pedras)
print("A Catapulta lançará {:.0f} pedras em {} baterias de {} minutos cada.".format(pedras, baterias, minutos))

"""
nome = input("Digite o seu nome: ")
sobrenome = input("Digite o seu sobrenome: ")

print("{} {}".format(nome, sobrenome))
"""
