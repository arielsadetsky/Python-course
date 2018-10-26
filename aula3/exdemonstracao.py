try:
    n = input('digite um número:')
    n = int(n)
    if n % 2 == 0:
        print('par.')
    else:
        print('impar')
except ValueError:
    res = [ord(x) for x in n]
    res = sum(res) 
    if res % 2 == 0:
        print('par {}'. format(res))
    else:
        print('impar {}'.format(res))
except Exception:
    print('tratamento genérico')
print ('não parei a execução.')
