# Projeto 3 - Chute um número
# objeto: Criar uma algorítimo que gera um valor aleatório e eu tenho q ficar tentando o número até eu acertar
import random
import PySimpleGUI as sg

class ChuteONumero:
    def __init__(self):
        self.valor_aleatorio = 0
        self.valor_minimo = 1
        self.valor_maximo = 100
        self.tentar_novamente = True

    def iniciar(self):
        # Layout
        layout = [
            [sg.Text('Seu chute', size=(39,0))],
            [sg.Input(size=(18,0),key='ValorChute')],
            [sg.Button('Chutar')],
            [sg.Output(size=(39,10))]
            
        ]
        # Criar uma janela
        self.janela = sg.Window('Chute o numero!', layout= layout)
       


        self.gerar_numero_aleatorio()
        try:
            while True:
                # Receber valores
                self.evento, self.valores = self.janela.Read()
                # Fazer algumas coisas 
                if self.evento == 'Chutar':
                    self.valor_do_chute = int(self.valores['ValorChute'])
                    while self.tentar_novamente == True:
                        if self.valor_do_chute > self.valor_aleatorio:
                            print('Chute um valor mais baixo')
                            break
                        elif self.valor_do_chute < self.valor_aleatorio:
                            print('Chute um valor mais alto')
                            break
                        if self.valor_do_chute == self.valor_aleatorio:
                            self.tentar_novamente = False
                            print('PARABÉNS VOCÊ ACERTOU!!')
                            break
        except:
            print('Favor digitar anepnas numeros!')
            self.iniciar()




    def gerar_numero_aleatorio(self):
        self.valor_aleatorio= random.randint(self.valor_minimo, self.valor_maximo)


chute = ChuteONumero()
chute.iniciar()