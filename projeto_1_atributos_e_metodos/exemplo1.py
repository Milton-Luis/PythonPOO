class Carro:
    
    # Método construtor
    def __init__(self, modelo: str, marca: str, ano: int, cor: str) -> None:
        
        # Atributos
        self.modelo = modelo
        self.marca = marca
        self.ano = ano
        self.cor = cor

    # Métodos
    def descriçao(self):
        return f"O carro é um {self.modelo}, marca {self.marca} de {self.ano} na cor {self.cor}"
    
    def ligar(self):
        return f"{self.modelo} está ligado"
    
    def meme(self):
        return f"Hoje o dia tá igual aquele carro, o {self.modelo} {self.cor}"
    

celta = Carro("Celta", "Chevrolet", 2010, "preto")
print(celta.descriçao())
print(celta.ligar())
print(celta.meme())