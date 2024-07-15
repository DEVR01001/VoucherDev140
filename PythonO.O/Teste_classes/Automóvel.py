class Auto:
    def __init__(self,marca,cor,ano,placa="ABC-1234"):
        self.marca= marca
        self.cor= cor
        self.ano= ano
        self.placa= placa


    def ligar(self):
            print(f"{self.marca} ligando")

    def getDados(self):
            print(f"Marca: {self.marca}")
            print(f"Cor: {self.cor}")
            print(f"Ano: {self.ano}")
            print(f"Placa: {self.placa}")


carro1= Auto("Audi","Prata", 2023, "BGJ-2342")
carro1.getDados()


carro1.ligar()