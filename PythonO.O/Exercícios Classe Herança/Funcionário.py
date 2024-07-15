# 6 - Classe Funcionário: Crie uma super classe que modele um Funcionário genérico. Esta classe deve possuir os seguintes atributos:​

# Nome;​

# Matricula;​

# Salario;​

# Método:​

# Bater_ponto(): deve criar uma lista de pontos do funcionário, pode ser booleana 0 ou 1;​

# Subclasses:​

# Defina as subclasses de Funcionário, exemplo Vendedor e Gerente. Após a criação das subclasses você deve criar atributos e métodos específicos de cada subclasse;​

# Ex: atributo comissão e método bater_meta() para Vendedor e atributo senha para o Gerente.​





class Funcionario:
    def __init__(self,nome,matricula,salario,ponto=True):
        self.nome= nome
        self.matricula=matricula
        self.salario=salario
        self.ponto= ponto



    def Bater_Ponto(self):
        if self.ponto == True:
            print("Ponto Batido")





class Vendedor(Funcionario):
    def __init__(self, nome, matricula, salario,comissao):
        super().__init__(nome, matricula, salario)
        self.comissao =comissao
    

    def Comissão(self):
        calculo= (self.comissao / 100) * self.salario
        calculo= self.salario + calculo
        print(f" O seu sálario original é de {self.salario} R$ com uma comição de {self.comissao} %, resulta num salario de {calculo}R$")




    def Meta_Bater(self,meta,vendas):
      calculo= meta-vendas
      if vendas > meta:
          print(f"Meta de {meta}R$ no mês batida. Vendas foram de {vendas}R$.\n Sobra de vendas foi de {calculo}R$")
      elif meta < vendas:
          print(f"Meta de {meta} não batida. Vendas foram de {vendas}R$.")
          



class Gerente(Funcionario):
    def __init__(self, nome, matricula, salario,senha):
        super().__init__(nome, matricula, salario)
        self.senha= senha

    def set_Senha(self,novasenha):
        self.senha = novasenha


        
    def GetSenha(self):
        print({self.senha}) 



        

funcionario1= Vendedor("Rafael",123456789,5000,3)


funcionario1.Bater_Ponto()
print("="*100)

funcionario1.Comissão()
print("="*100)

funcionario1.Meta_Bater(1000,1100)
print("="*100)

funcionario2= Gerente('Matheus',123456789,7000,3082004)

funcionario2.GetSenha()
print("="*100)
funcionario2.set_Senha(987654321)

funcionario2.GetSenha()

print("="*100)
funcionario1.Bater_Ponto()