class Pai:
    a = 'classe pai'

class Mae:
    b = 'classe mae'

class Filho(Pai, Mae):
    c = 'classe filho'

    objeto = Filho()

print(objeto.a, objeto.b, objeto.c)