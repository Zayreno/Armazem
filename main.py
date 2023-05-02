from Peca import Peca
from Local import Local

listaPecas = [Peca('prego', 25, Local(4, 1)), Peca('prego', 14, Local(4, 1)),
              Peca('porca', 64, Local(7, 5))]

def quantidadeItems(x: int, y:int) -> int:
    soma = 0
    for i in listaPecas:
        if i.local.x == x and i.local.y == y:
            soma += i.quantidade
    return soma

def listarArtigos():
    for x in listaPecas:
        x.print()

def desenhaArmazem():
    for x in range(0, 10):
        for y in range(0, 10):
            quantidade = quantidadeItems(x, y)
            print(str(quantidade) + "\t", end="")

        print("")

escolha = -1
while escolha != 0:
    escolha = int(input("\n2. Desenhar armazém\n1. Listar artigos\n0. Sair\n"))
    match escolha:
        case 0:
            break
        case 1:
            listarArtigos()
        case 2:
            desenhaArmazem()
        case _:
            print("Escolha inválida")

