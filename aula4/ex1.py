convidados = []
x = len(convidados)
def adicionar(nome):
    global convidados
    convidados.append(nome)
while(True):
    nome = input('digite o nome ou sair:')
    if nome.strip().lower() == 'sair':
        break
    adicionar(nome)
print(convidados)

