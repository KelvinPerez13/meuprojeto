header = "a versao deste arquivo e a numero 2"

class testes:
    def __init__(self, nome: str, idade: int, altura: int):
        self.nome = nome 
        self.idade = idade
        self.altura = altura 
        
    def meunome(self):
        return print(self.nome)


kelvin = testes('kelvin', 30, 173) 

kelvin.meunome()