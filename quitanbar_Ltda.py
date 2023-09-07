

class Copo:
    def __init__(self, estado, conteudo):
        self.estado = estado
        self.conteudo = conteudo

    def mudanca_estado(self):
        print(f'O que temos pra hoje é (A)-água\t (C)-cerveja\t (R)-refrigerante (S)-só olhondo mesmo')
        op = input().upper()

        if op == 'S':
            print('Capa o gato daqui!!')
        elif op == 'A':
            print('Água com (1) ou sem gás (2)?')
            escolha = int(input('Entre com o valor: '))
            self.produto_agua(escolha)
            self.estado = 'cheio'
            print(f'{self.estado}, {self.conteudo}')
        elif op == 'C':
            print('Qual a cerveja? 1 – Sko, 2 – Brahma, 3 – Antarctica')
            escolha = int(input('Entre com o valor: '))
            self.produto_cerveja(escolha)
            self.estado = 'cheio'
            print(f'{self.estado}, {self.conteudo}')
        elif op == 'R':
            print('Qual a refrigerante? 1 – Coca-Cola, 2 – Fanta, 3 – Jesus')
            escolha = int(input('Entre com o valor: '))
            self.produto_refrigerante(escolha)
            self.estado = 'cheio'
            print(f'{self.estado}, {self.conteudo}')

    def produto_agua(self, tipo):
        if tipo == 1:
            self.conteudo = 'Água com gás'
            return self.conteudo
        elif tipo == 2:
            self.conteudo = 'Água sem gás'
            return self.conteudo
    def produto_cerveja(self, marca):
        if marca == 1:
            self.conteudo = 'Sko'
            return self.conteudo
        elif marca == 2:
            self.conteudo = 'Brahma'
            return self.conteudo
        elif marca == 3:
            self.conteudo = 'Antarctica'
            return self.conteudo
    def produto_refrigerante(self, marca):
        if marca == 1:
            self.conteudo = 'Coca-Cola'
            return self.conteudo
        elif marca == 2:
            self.conteudo = 'Fanta'
            return self.conteudo
        elif marca == 3:
            self.conteudo = 'Jesus'
            return self.conteudo


meu_copo = Copo('vazio', None)
meu_copo.mudanca_estado()