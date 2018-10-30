class Conta():

    def __init__(self, titular, numero, saldo=0):
        self.titular = titular
        self.numero = numero
        self.saldo = saldo
    def depositar(self, valor):
        self.saldo += valor
        return self.saldo
    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            return 'saque realizado com sucesso'
        else:
            raise ValueError('saldo insuficiente{}'.format(self.saldo))
    def transferir(self, valor, conta):
        try:
            self.sacar(valor)
            conta.depositar(valor)
            return 'transferencia realizada com sucesso!'
        except ValueError as e:
            print(e)
            return 'não foi possível realizar a transferencia'
        except Exception:
            return 'conta destino inválida'
    def __str__(self):
        return 'conta: {} titular: {}'.format (
        self.numero, self.titular
        )

        
c1 = Conta('daniel', 12355, 1000)
c2 = Conta('maria', 2939131, 1000)
c1.transferir(500,c2)
print(c1.saldo)
print(c2.saldo)



            

    



