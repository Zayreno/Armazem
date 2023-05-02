from Local import Local


class Peca:
    def __init__(self, nome: str, quantidade: int, local: Local):
        self.nome = nome
        self.quantidade = quantidade
        self.local = local

    def print(self):
        print(self.nome)
        print(self.quantidade)
        self.local.print()
