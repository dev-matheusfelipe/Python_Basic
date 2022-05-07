class Pessoa:
    def __init__(self, nome, idade, sexo, falando=False, comendo=False):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.falando = falando
        self.comendo = comendo
    
    def falar(self, assunto):
      if self.falando:
        print(f'{self.nome} já falando')
        return
      print(f'{self.nome} está falando sobre {assunto}')
      self.falando = True

    def para_falar(self):
      if self.falando:
        print(f'{self.nome} parou de falar')
        self.falando = False
        return
      print(f'{self.nome} já parou de falar')

    def comer(self, comida):
      if self.comendo:
        print(f'{self.nome} já está comendo')
        return
      print(f'{self.nome} está comendo {comida}')
      self.comendo = True  

    def para_comer(self):
      if self.comendo:
        print(f'{self.nome} parou de comer')
        self.comendo = False
        return
      print(f'{self.nome} já parou de comer')
        
if __name__ == "__main__":

    p1 = Pessoa("João", 19,"M")
    p2 = Pessoa("Maria", 25,"F")
    #print(p1)
    #print(p2)
    #print(p1.nome, p1.idade, p1.sexo)


    #p1.falar('Futebool')
    #p1.falar('Carros')
    #p1.para_falar()
    #p1.para_falar()
    #p1.falar('F1')

    p1.comer('Morango')
    p1.comer('Morango')
    p1.para_comer()
    p2.comer('Abacaxi')
    p2.comer('Abacaxi')
    p2.para_comer()
    p2.comer('Melancia')
