class Dog():
   
    def __init__(self, nome, raca, idade, energia):
        self.nome = nome
        self.raca = raca
        self.idade = idade
        self.energia = 5

    def latir(self):
        print(self.nome)
        print('AUAUauauau...')

    def dormir(self):
        self.energia = 5
        print('ZzZzZzZz...{}'.format(self.energia))

    def andar(self):
        if self.energia:
            self.energia -= 1
        print('andando{}'.format(self.energia))

dog1 = Dog('bilu','pitbull', 1, 10)




