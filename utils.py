
class testes:
    def __init__(self, nome: str, idade: int, altura: int):
        self.nome = nome 
        self.idade = idade
        self.altura = altura 
        
    def meunome(self):
        return print(self.nome)

    def idade(self):
        return print(self.idade)

kelvin = testes('kelvin', 30, 173) 

kelvin.meunome()