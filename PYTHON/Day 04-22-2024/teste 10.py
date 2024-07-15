#### Faça um Programa que receba 3 entradas de dados e informe qual tipo de dados está ####
#### rmazenado na variável se é do tipo: int, float ou string ####

var1= input("Digite algo ")
var2= int(input("Digite outras coisa: "))
var3= float(input("Digite uma terceira coisa: "))

if(isinstance(var1,str)):
    print("string")

if(isinstance(var1,int)):
    print("inteiro")

if(isinstance(var1,float)):
    print("float")


