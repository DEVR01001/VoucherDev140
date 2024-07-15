# 2 - Classe Pessoa: Crie uma super classe que modele uma Pessoa. Esta classe deve possuir os seguintes atributos:​

# Matricula; Nome; Idade;  ​

# Subclasses:​

# Defina as subclasses de Pessoa serão Aluno e Professor, estas devem conter além dos atributos herdados de Pessoa seus atributos identificadores, ex: Classe Aluno (NOTAS; MEDIA). ​

# Classe Professor (Formacao, Disciplina, Carga Horária e Salario)​

# Você deve criar métodos específicos para cada subclasse, ex: calcular_media, estudar, lecionar.​




class Pessoa():
    def __init__(self,Matricula,Nome,Idade):
        self.Matricula= Matricula
        self.Nome= Nome
        self.Idade= Idade



class Aluno(Pessoa):
    def __init__(self, Matricula, Nome, Idade,Notas):
        super().__init__(Matricula, Nome, Idade)
        self.Notas= Notas

    
    def Calcular_Media(self):
        calcular_media= self.Notas/4
        return print(f"A média do aluno {self.Nome} é {calcular_media}")
        
    def GetEstudar(self):
        print(f"Agora vou estudar")


class Professor(Pessoa):
    def __init__(self, Matricula, Nome, Idade, Formacao,Diciplica,Carga_Horaria,Salario):
        super().__init__(Matricula, Nome, Idade)
        self.Formacao= Formacao
        self.Diciplina = Diciplica
        self.Carga_Horaria= Carga_Horaria
        self.Salario= Salario

    def GetLecionar(self):
        print(f"Tenho que dar aula hoje!!!")
    


i = 0
soma_notas= 0
while i < 4:
    nota= float(input("Digite sua nota: "))
    i+=1
    soma_notas+= nota


aluno1= Aluno(1987654,"Rafael",19,soma_notas)


aluno1.Calcular_Media()
print("="*100)
aluno1.GetEstudar()

print("="*100)

professor1= Professor(12345678,"Thiago",25,"Analise e Desvolvimento de Sistemas","Algoritmo",40,7000)

professor1.GetLecionar()
