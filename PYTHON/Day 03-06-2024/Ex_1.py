# https://pythonacademy.com.br/
#criação dicionario


pessoas= {
    'nome_1': 'Rafel Rodrigues dos Santos', 
    'idade_1': '19', 
    'cidade_1': 'Campo Grande', 
    'profissão_1': 'Estudante',
    'nome_2': 'Matheus',
    'idade_2': '27',
    'cidade_2': 'Campo Grande',
    'profissão_2': 'Dev Pleno',

    }
print(pessoas)
print("="*180)
#criar uma váriavel para mandar um print em alguma keyword especifica do dicionário

# idade = pessoas['idade_1']
# nome = pessoas['nome_1']

# print sem necessariamente criar uma váriavel 
print(pessoas['nome_1'])
print(pessoas['idade_1'])
print("="*180)

# Mostras todas as chaves do dicionário

print(pessoas.keys())
print("="*180)

# Adicionar uma nova chave com um valor no dicionario
pessoas['e_mail']= 'rafa.rodriques12@gmail.com' 
print(pessoas['e_mail'])
print("="*180)

# print keword e valor com for

for chave in pessoas.keys():
  print(f'Chave = {chave} e Valor = {pessoas[chave]}')
print("="*180)

# perccorer for em um dicionário, apenas o valor das keyword

for i in pessoas.values():
    print(f"Valor: {i}")
print("="*180)

# percorrer dicionário com função
print(pessoas.items())
print("="*180)

#remover um item do dicionário
pessoas.pop('idade_2')
print(pessoas)
print("="*180)

#remover um tiem com del do dicionário
del pessoas['nome_1']
print(pessoas)
print("="*180)

#limpar um dicionário

pessoas.clear()
print(pessoas)