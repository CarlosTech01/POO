from pathlib import Path
import sys


PASTA_ATUAL = Path(__file__).resolve().parent
PASTA_PAI = PASTA_ATUAL.parent

if str(PASTA_PAI) not in sys.path:
    sys.path.append(str(PASTA_PAI))

from aluno import Aluno
from curso import Curso


def cadastrar_cursos():
    cursos = []
    quantidade = int(input("Quantos cursos deseja cadastrar? "))

    for i in range(quantidade):
        print(f"\nCadastro do curso {i + 1}")
        nome = input("Nome do curso: ").strip()
        duracao = int(input("Duração em semestres: "))
        cursos.append(Curso(nome, duracao))

    return cursos


def cadastrar_alunos(cursos):
    alunos = []
    quantidade = int(input("Quantos alunos deseja cadastrar? "))

    for i in range(quantidade):
        print(f"\nCadastro do aluno {i + 1}")
        nome = input("Nome: ").strip()
        matricula = input("Matrícula (8 a 10 dígitos): ").strip()

        print("\nCursos disponíveis:")
        for indice, curso in enumerate(cursos, start=1):
            print(f"{indice}. {curso.nome}")

        while True:
            escolha = input("Digite o número do curso: ").strip()
            if escolha.isdigit() and 1 <= int(escolha) <= len(cursos):
                curso_escolhido = cursos[int(escolha) - 1]
                break
            print("Escolha inválida.")

        alunos.append(Aluno(nome, matricula, curso_escolhido))

    return alunos


def adicionar_notas(alunos):
    for aluno in alunos:
        print(f"\nAdicionando notas para {aluno.get_nome()}:")
        for i in range(2):
            while True:
                entrada = input(f"Digite a nota {i + 1} para {aluno.get_nome()}: ").strip()
                if not entrada:
                    print("Entrada vazia. Digite uma nota válida.")
                    continue
                try:
                    aluno.adicionar_nota(float(entrada))
                    break
                except ValueError as erro:
                    print(erro)
