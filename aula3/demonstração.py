#!/urs/bin/python3
nome = input('digite o nome do arquivo:')
shebang = '#!/usr/bin/python3'
try:
    with open(nome, 'x') as arq:
        arq.write(shebang)
except FileExistsError:
    with open(nome,'r') as arq:
        conteudo = arq.readlines()
    if conteudo:
        if conteudo[0] != shebang:
            conteudo.insert(0,shebang)
        with open(nome,'w') as arq:
            arq.writelines(conteudo)
    else:
        with open(nome,'a') as arq:
            arq.writelines(shebang)

