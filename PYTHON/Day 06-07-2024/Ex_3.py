def preçoitem():
    preço= 1.99
    for quantidades in range(1,51):
        total= quantidades*preço
        print(f"{quantidades}, R${total}")

preçoitem()

