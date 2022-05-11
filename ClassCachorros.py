class Cachorros:

    def __init__(self, nome, cor_de_pelo, idade, tamanho, racao, comendo=False, beberAgua=False, latindo=False, correndo=False):
        self.nome = nome
        self.cor_de_pelo = cor_de_pelo
        self.idade = idade
        self.tamanho = tamanho
        self.racao = racao
        self.beberAgua = beberAgua
        self.comendo = comendo
        self.latindo = latindo
        self.correndo = correndo

    def latir(self):
        if self.comendo:
            print(f'{self.nome} está comendo não pode latir.')
            return

        if self.latindo:
            print(f'{self.nome} já está latindo.')
            self.latindo = True
            return
        print(f'{self.nome} está latindo au au.')

    def parar_latir(self):
        print(f'{self.nome} parou de latir.')
        self.latindo = False
        return

    def correr(self):
        print(f'{self.nome} já está correndo.')
        self.correndo = True
        return

    def parar_correr(self):
        print(f'{self.nome} parou de correr.')
        self.correndo = False
        return

    def comer(self, racao):
        if self.comendo:
            print(f'{self.nome} já está comendo.')

        if self.latindo:
            print(f'{self.nome} não pode comer está latindo.')

        print(f'{self.nome} está comendo {racao}.')
        self.comendo = True
        return

    def parar_comer(self):
        if self.comendo:
            print(f'{self.nome} parou de comer.')
            self.comendo = False
            return
        print(f'{self.nome} já parou de comer.')

    def berberAgua(self, racao):
        if self.beberAgua:
            print(f'{self.nome} já está bebendo agua.')

        if self.latindo:
            print(f'{self.nome} não pode beber agua latindo.')

        print(f'{self.nome} está bebendo agua.')
        self.beberAgua = True
        return

    def parar_berberAgua(self):
        if self.beberAgua:
            print(f'{self.nome} parou de beber agua.')
            self.beberAgua = False
            return
        print(f'{self.nome} já parou de beber agua.')



#Criando o Objeto
cachorro1 = Cachorros('Toby', 'marrom', 5, 'grande')
cachorro2 = Cachorros('Max', 'preto', 3, 'pequeno')

#Testando os parametros do construtor cachorro1.
print(cachorro1.nome)
print(cachorro1.idade, 'anos')
print(cachorro1.cor_de_pelo)
print(cachorro1.tamanho)

#testando as Ações cachorro1
cachorro1.latir()
cachorro1.correr()

#Testando os parametros do construtor cachorro2.
print(cachorro2.nome)
print(cachorro2.idade, 'anos')
print(cachorro2.cor_de_pelo)
print(cachorro2.tamanho)

#testando as Ações cachorro2
cachorro2.latir()
cachorro2.correr()


