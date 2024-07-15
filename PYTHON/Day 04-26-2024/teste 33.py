#### Um produto vai sofrer aumento de acordo com a tabela abaixo. Leia o preço antigo, calcule e ####
#### escreva o preço novo, e escreva uma mensagem em função do preço novo (de acordo com a ####
#### segunda tabela). ####


#### PREÇO ANTIGO         |PERCENTUAL DE AUMENTO #### 
#### até R$ 50            |   5% #### 
#### entre R$ 50 e R$ 100 |   10% #### 
#### acima de R$ 100      |   15% #### 

preçoantigo= float(input("Digite o preço antigo do produto: "))

if( preçoantigo > 0 and preçoantigo <=50):
    calculo1= preçoantigo*(5/100)
    preçonovo= calculo1+preçoantigo
    print(f" O preço novo é de {preçonovo}")
elif( preçoantigo > 50 and preçoantigo <=100):
    calculo1= preçoantigo*(10/100)
    preçonovo= calculo1+preçoantigo
    print(f" O preço novo é de {preçonovo}")
elif( preçoantigo > 100):
    calculo1= preçoantigo*(15/100)
    preçonovo= calculo1+preçoantigo
    print(f" O preço novo é de {preçonovo}")



