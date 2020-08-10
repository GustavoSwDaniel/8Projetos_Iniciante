# Projeto 3 - Chute um número
# objeto: Criar uma algorítimo que gera um valor aleatório e eu tenho q ficar tentando o número até eu acertar
import random

class ChuteONumero:
    def __init__(self):
        self.valor_aleatorio = 0
        self.valor_minimo = 1
        self.valor_maximo = 100
        self.tentar_novamente = True

    def iniciar(self):
        self.gerar_numero_aleatorio()
        self.pedir_valor_aleatorio()
        try:
            while self.tentar_novamente == True:
                if self.valor_do_chute > self.valor_aleatorio:
                    print('Chute um valor mais baixo')
                    self.pedir_valor_aleatorio()
                elif self.valor_do_chute < self.valor_aleatorio:
                    print('Chute um valor mais alto')
                    self.pedir_valor_aleatorio()
                if self.valor_do_chute == self.valor_aleatorio:
                    self.tentar_novamente = False
                    print('PARABÉNS VOCÊ ACERTOU!!')
        except:
            print('Favor digitar anepnas numeros!')

    
    def pedir_valor_aleatorio(self):
        self.valor_do_chute = int(input('Chute um número: '))

    def gerar_numero_aleatorio(self):
        self.valor_aleatorio= random.randint(self.valor_minimo, self.valor_maximo)


chute = ChuteONumero()
chute.iniciar()