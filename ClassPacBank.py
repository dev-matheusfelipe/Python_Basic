class PacBank:

    def __init__(self, numero, titular, saldo, limite):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def imprimeSaldo(self):
        print(f"{self.titular} tem saldo: R$ %.2f" % self.saldo)

    def saca(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            return True
        else:
            print("Saldo insuficiente para está operação.")
            return False

    def deposita(self, valor):
        self.saldo += valor

    def transfere(self, cc_destino, valor):
        if self.saca(valor) == True:
            cc_destino.deposita(valor)


###  Testando a classe PacBank ###
minhaConta = PacBank(123, "junior", 500, 1000)
suaConta = PacBank(321, "Senior", 1500, 2000)
minhaConta.deposita(300)
minhaConta.deposita(200)
minhaConta.imprimeSaldo()              # Saldo Atual: R$ 1.000,00
minhaConta.saca(100)                   # Saldo Atual: R$  900,00
minhaConta.imprimeSaldo()              # Meu saldo:   R$ 1.500,00
suaConta.imprimeSaldo()                # Seu saldo:   R$  500,00
minhaConta.transfere(suaConta, 400)    # Saldo atual: R$ 500,00
minhaConta.imprimeSaldo()              # Meu saldo: R$ 500,00
suaConta.imprimeSaldo()                # Seu saldo: R$ 1.900,00
minhaConta.saca(600)                   # Erro: saldo insuficiente
