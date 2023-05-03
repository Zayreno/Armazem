from Peca import Peca
from Local import Local

listaPecas = [Peca('prego', 25, Local(4, 1)), Peca('parafuso', 14, Local(5, 8)),
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
    for x in range(1, 11):
        for y in range(1, 11):
            quantidade = quantidadeItems(x, y)
            print(str(quantidade) + "\t", end="")

        print("")


def editaQuantidade():
    nomePeca = input("Indique o nome da peça:\n")
    for q in listaPecas:
        if nomePeca == q.nome:
            q.quantidade = int(input("Indique quantas peças lá estão:\n"))
            break

def adicionarPecas():
    nomePeca = input("Indique o nome da peça:\n")
    quantidadePeca = int(input("Indique quantas peças lá estão:\n"))
    x, y = input("Indique onde quer guardar as peças:(X Y)\n").split(" ")
    x = int(x)
    y = int(y)

    meuLocal = Local(x, y)

    for i in listaPecas:
        if i.nome == nomePeca:
            i.quantidade = i.quantidade + quantidadePeca
            print("Já lá tinha peças, o total agora é de " + str(i.quantidade) + " peças.")
        elif i.local == meuLocal:
            print("Já se encontram outras peças aí.")

    novaPeca = Peca(nomePeca, quantidadePeca, meuLocal)
    listaPecas.append(novaPeca)


escolha = -1
while escolha != 0:
    escolha = int(input("\n0. Sair\n1. Listar artigos\n2. Desenhar armazém\n"
                        "3. Editar quantidades\n4. Adicionar peças\n"))
    match escolha:
        case 0:
            break
        case 1:
            listarArtigos()
        case 2:
            desenhaArmazem()
        case 3:
            editaQuantidade()
        case 4:
            adicionarPecas()
        case _:
            print("Escolha inválida")

