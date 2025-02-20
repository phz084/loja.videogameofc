nomes  = []
def adicionar_nome(nomes):
    nomes.append(input('digite um nome para colocar na sua lista: '))
for i in range(5):
    adicionar_nome(nomes)
print(nomes)

a = int(input("digite um numero: "))
def calcul_paridade(a):
    if a % 2 == 0:
        print("par")
    else:
        print('impar')

calcul_paridade(a)