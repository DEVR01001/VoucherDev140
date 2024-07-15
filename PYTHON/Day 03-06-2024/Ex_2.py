amigos = {
    'amigo_1': 'Matheus',
    'amigo_2': 'Arthur',
    'amigo_3': 'Marcos',
    'amigo_4': 'Lenandro',
    'amigo_5': 'Maycon'


}
# Percorrer o dicionário
for i in amigos.keys():
    print(f"{i}: {amigos[i]}")

print("="*180)

# Verificar se o novo nome já está no dicionário

for i in amigos.keys():
    amigo_6= (input("Digite nome de um novo amigos: "))
    if amigo_6 in amigos.values():
        print("Ele está na lista")
        break
    else:
        print("Ele não está na lista")
        break





