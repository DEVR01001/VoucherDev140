from Students import Students
from Teacher import Teacher

matricula= input(F"Digite o número da mátricula: ")
nome= input(F"Digite o nome do aluno/aluna: ")
idade= input(F"Digite o idade: ")
nota= input(F"Digite o nota: ")

aluno1= Students(matricula,nome,idade,nota)
aluno1.mostrardados()