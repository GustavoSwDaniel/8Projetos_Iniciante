# Projeto 7 - Jogo de Aventura
# Um jogo de decisões onde eu terei que criar varios finais diferentes baseados nas respostas que forem dadas

# Eu quero chegar a finais difrente na minha historia, de acordo com as resposta que eu passe para o programa

# Qual é o cenario: Eu estou numa guerra entre duas nações, é nós temos 2 lados: Lado A, Lado B. Somente o ladoA irá vencer e o ladoB irá perder: Então tenho que tomar as decisões corretas para chegar até a vitoria, que somente o ladoA ieá conseguir!
import PySimpleGUI as sg



class JogoDeAventura:
    def __init__(self):
        self.perguntas1 = 'Você nasceu no norte ou sul? (n/s)' # Norte = LadoA, Sul = LadoB
        self.perguntas2 = 'Você prefere a espada ou escudo? (espada/escuto)' #Espado = LadoA = escuto LadoB
        self.perguntas3 = 'Qual é a sua espcialidade?(linha de frente/tatico) ' # Linha de frente = LadoA, tático = LadoB
        self.finalHistoria1 = 'Você será um heroi na linhas de frente!'
        self.finalHistoria2 = 'Você será um heroi pretegendo nossa tropas!'
        self.finalHistoria3 = 'Você irá se sacrifica na batalha!'
        self.finalHistoria4 = 'Você não é capaz de lutar nessa batalha!'

    
    def iniciar(self):
        layout = [
            [sg.Output(size=(30,10), key='respotas')],
            [sg.Input(size=(25,0), key='escolha')],
            [sg.Button('Iniciar'),sg.Button('Responder'),sg.Button('Sair')]
        ]
        
        self.janela = sg.Window('Jogo de Aventura!', layout=layout)
        while True:
            self.ler_valores()

            if self.evento == 'Iniciar':
                print(self.perguntas1)
                self.ler_valores()
                if self.valores['escolha'] == 'n':
                    print(self.perguntas2)
                    self.ler_valores()
                    if self.valores['escolha'] == 'espada':
                        print(self.finalHistoria1)
                    if self.valores['escolha'] == 'escudo':
                        print(self.finalHistoria2)
                if self.valores['escolha'] == 's':
                    print(self.perguntas3)
                    self.ler_valores()
                    if self.valores == 'linha de frente':
                        print(self.finalHistoria3)
                    if self.valores['escolha'] == 'tatico':
                        print(self.finalHistoria4)
            if self.evento == 'Sair':
                quit()

    def ler_valores(self):
        self.evento, self.valores = self.janela.Read()

jogo = JogoDeAventura()
jogo.iniciar()