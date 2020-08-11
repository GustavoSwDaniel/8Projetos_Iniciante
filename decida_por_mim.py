# Projeto 5 - DEcida por mim
# Faça uma pergunta para o prgrama e ele terá que te dar uma resposta
import random
import PySimpleGUI as sg

class DecidaPorMim:
    def __init__(self):
        self.respostas = [
            'Com certeza, você deve fazer isso!',
            'Não sei, você que sabe',
            'Não faz isso Não!',
            'Acho que tá na hora certa'
        ]


    def iniciar(self):
        # Layout
        layout = [
            [sg.Text('Faça sua pergunta:')],
            [sg.Input()],
            [sg.Output(size=(50,10))],
            [sg.Button('Decida por min')],
            [sg.Button('Sair')]
        ]
        # Criar uma janela
        self.janela = sg.Window('Decida por Mim!', layout=layout)
        while True:
            # Ler os valores
            self.evento, self.valores= self.janela.Read()
            # Fazer algo com os valores
            if self.evento == 'Decida por min':
                print(random.choice(self.respostas))
            else:
                self.janela.Close()

decida = DecidaPorMim()
decida.iniciar()