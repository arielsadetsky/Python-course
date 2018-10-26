ling = input ('qual a melhor linguagem de programação?')
ling = ling.strip().lower()
if ling == 'python':
        print('você está no caminho certo')
elif ling == 'html' or ling == 'css':
    raise ValueError('isso não é uma linguagem de programação')
else:
        print('mude para python!')

exit()
letras = ['a','b']
try:
    print('letras[2]')
except IndexError as e:
    print('a lista contem apenas {} elementos'.format(len(letras)))
    print(e)
    print(ling.get('daniel'))





     