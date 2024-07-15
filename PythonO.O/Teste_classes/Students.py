class Students: #Definição da classe
    def __init__(self, matricula,nome,idade,nota): #m= método construtor
        self.matricula = matricula # Atributo
        self.nome= nome # Atributo
        self.idade= idade # Atributo
        self.nota= nota # Atributo

    def hello(self): # Método
        print(f"Hello {self.nome}")

    def mostrardados(self):
        print(f"Mostre os dados:")
        print (f"{self.matricula}")
        print (f"{self.nome}")
        print (f"{self.idade}")
        print (f"{self.nota}")
    

# aluno= Students(1212,"Rafael",18,80) # Atribui a uma váriavel os atributos de uma classe

# print(aluno.nome)  # Chamada de posição da lista da classe
# print(aluno.nota)  # Chamada de posição da lista da classeS

# aluno_2= Students(1514,"Matheus", 27,10) #Atribui  a uma váriavel os atributos de uma classe

# print(aluno_2.nome)  # Chamada de posição da lista da classe

# aluno_2.hello() # Chamada de método dentro de uma classe

# aluno_2.nome = "Leandro" # Editar(Atribuir) a atribuição de uma váriavel
# aluno_2.hello()

# aluno.mostrardados() # Chamada para mostrar todos os dados

# print("="*100)

# from Teacher import professor_1

# print(professor_1)