class Pilha(object):
    def __init__(self):
        self.itens = []
 
    def adicionar(self, valor):
        self.itens.append(valor)
 
    def excluir(self):
            return self.itens.pop(-1)
 
    def imprimir(self):
        for i in range(len(self.itens)):
             print(self.itens) 
        
