class Pessoa:
    def __init__(self, ID=0,nome=None):
        self.ID= ID
        self.nome= nome

    def Hello(self):
        print(f"Hello {self.nome}")

    
pessoa1= Pessoa()

print(pessoa1.ID)

name_pessoa= input("Digite seu nome: ")
id_pessoa= input("Digite seu ID: ")

pessoa1.nome= name_pessoa
pessoa1.ID= id_pessoa

print(pessoa1.ID)
pessoa1.Hello()