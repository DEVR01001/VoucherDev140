# Importação de função especifica de um modulo  

from funções import soma

print(soma(2,3))

#Importação de mais de uma função d eum módulo 

from funções import(div,mult)

multiplicação= mult(2,3)
adição= soma(2,1)


resultado= multiplicação - adição
print(resultado)

#Importação de todas as funções de um módulo (Simbolo é "*")

from funções import *

print(div(40,2))

print(subtração(43,34))

# Navegação entre diretórios >> ./(nomepacote) para avançar de pastas
# ../(nomepacote) para voltar a pasta 