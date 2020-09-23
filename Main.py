from Pilha import Pilha


pilha = Pilha()
pilha.adicionar(10)
pilha.adicionar(5)
pilha.adicionar(15)
pilha.adicionar(20)
valor = input("Digite um valor: ")
pilha.adicionar( valor )


resp= int(input("Deseja Excluir o item do topo? 1- Sim 2- Não: "))
if resp == 1:
    pilha.excluir()
    pilha.imprimir()
else:
    print("Nada foi excluido. ")
    pilha.imprimir()
