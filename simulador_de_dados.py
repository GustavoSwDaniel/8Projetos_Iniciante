# Simular o uso de um dado, gerando um valor de 1 até 6

import random
import PySimpleGUI as sg

class SimuladorDeDados:
    
    
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        # Layout
        self.layout = [
            [sg.Text('Jogar o dado?')],
            [sg.Button('Sim'), sg.Button('Não')]
        ]
        
    def iniciar(self):

        # Criar um janela
        self.janela = sg.Window('Simulador de Dado',layout=self.layout)
        # Ler os valores da tela
        self.eventos, self.valores = self.janela.Read()
        # Fazer alguma coisa com esse valores
      
        try:
            if self.eventos == 'Sim' or self.eventos == 'S':
                self.gerar_valor_do_dado()
            elif self.eventos == 'Não' or self.eventos == 'N':
                print('Agradecemos sua participação')
            else:
                print('Favor digitar sim ou não')
        except:
            print('Ocorreu um erro ao receber sua resposta!')

    def gerar_valor_do_dado(self):
        print(random.randint(self.valor_minimo, self.valor_maximo))


simulador = SimuladorDeDados()
simulador.iniciar()
