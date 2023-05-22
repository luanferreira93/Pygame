class Cachorro:
    # método construtor
    def __init__(self, nome, cor, idade, tamanho):
        # atributos
        self.nome = nome
        self.cor = cor
        self.idade = idade
        self.tamanho = tamanho

    # método da classe Cachorro
    def latir(self):
        print('AU AU AU')
    def correndo(self):
        print(f'O {self.nome} está correndo....')

# Instanciando um objeto criando um objeto partir da classe
cachorro_1 = Cachorro('Pretinho','Preto',2,'Grande')#método construtor

cachorro_1.idade = 8

cachorro_1.correndo()