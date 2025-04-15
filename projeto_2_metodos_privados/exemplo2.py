class Pessoa:
    def __init__(self, nome:str, idade:int, cpf:str) -> None:
        self.nome = nome
        self.idade = idade
        self.__cpf = cpf # Atributo privado, não pode ser acessado fora da classe

    def apresentar(self):
        """Este é um método publico, este pode ser acessado em qualquer parte do código"""

        return f"Olá, meu nome é {self.nome}, tenho {self.idade} anos e meu CPF é {self.__exibir_documento()}."

    def __exibir_documento(self):
        """Sempre que eu colocar __ antes do nome do método este será um método privado, este não poderá ser acessado fora da classe, só podendo ser acessados dentro da própria classe, igual como está em apresentar()
        São uteis quando precisamos evitar que certos dados sejam mostrados abertamente ao usuário, como senhas, CPF, etc."""
        return self.__cpf


pessoa = Pessoa("João", 30, "123.456.789-00")
print(pessoa.apresentar())  # Este método é público e pode ser acessado em qualquer
# pessoa.__exibir_documento()
pessoa.__cpf = "987.654.321-00"  # Isso não altera o valor do atributo privado
print(pessoa.__cpf)  # Este atributo é privado e não pode ser acessado fora da classe