# Crie um dicionário de tradução que mapei palvras de um idioma para outro ( por exemplo, ingles para espanhol). 
# Peça ao usuário uma palavra em ingles e , em seguida a tradução correrpondente



dicionario= {
    'mesa': 'table',
    'maça': 'apple',
    'papel': 'paper',
    'dedo': 'finger',
    'boca': 'mouth',
    'braço': 'hand',

}


palavra= input("Digite uma palavras para a tradução em ingles: ")

if palavra in dicionario.keys():
    print(f'{palavra}: {dicionario[palavra]}')
else: 
    print("Palavra não possui no dicionário")
    

