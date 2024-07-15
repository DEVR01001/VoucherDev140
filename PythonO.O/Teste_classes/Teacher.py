class Teacher:
    def __init__(self,Id_professor,nome,idade,CPF):
        self.Id_professor= Id_professor
        self.nome= nome
        self.idade= idade
        self.cpf= CPF
    
    def mostrar_dados(self):
        print(f"Dados professor Maneiro: Nome: {self.nome}, idade: {self.idade}, CPF: {self.cpf}, ID Professor: {self.Id_professor}")




# professor_1= Teacher(32454,'Thiago',37,"437.284.153-43") #Atribui  a uma váriavel os atributos de uma classe


# # print(professor_1.Id_professor)  # Chamada de posição da lista da classeS

# professor_1.mostrar_dados() # Chamada para mostrar todos os dados 


