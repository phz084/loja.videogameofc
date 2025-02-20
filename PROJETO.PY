nomes  = []
def adicionar_nome(nomes):
    nomes.append(input('digite um nome para colocar na sua lista: '))
for i in range(5):
    adicionar_nome(nomes)
print(nomes)