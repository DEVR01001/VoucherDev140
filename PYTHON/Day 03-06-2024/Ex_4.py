# Crie um dicionário  que represente o estoque de uma loja, com produtos como chaves e quantidades em estoque de valores.Permita que o usuário insira um produto e verifique 
# se ele está em estoque. Se tiver, informe a quantidade em estoque; caso contrário, informe que o produto não está disponivel. 



produtos= {
    'cadeira': 50,
    'mesa': 30,
    'sofá': 15,
    'hack': 5,
    'ventilador': 23,
    'lampada': 36,
    }
print(f"Estoque : {produtos}")


item= input("Insira um novo produto: ")

if item in produtos.keys():
    print(f'O produto: {item}, possui no estoque e sua quantidade é {produtos[item]}.')
else:
    print("Não está no estoque")

