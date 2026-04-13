class Curso:
    def __init__(self, nome, duracao):
        self.nome = nome.strip()
        self.duracao = int(duracao)

    def descricao(self):
        return f"Curso: {self.nome} | Duração: {self.duracao} semestres"
