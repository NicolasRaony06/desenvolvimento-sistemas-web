from questoes import Aluno, Curso

def cadastrarAluno():
    nome = input("Digite o nome do aluno: ")
    idade = int(input("Digite a idade do aluno: "))
    email = input("Digite o email do aluno: ")
    matricula = int(input("Digite a matrícula do aluno: "))

    return Aluno(nome, idade, email, matricula)

def cadastrarAlunoCurso():
    nome_aluno = input("Digite o nome do aluno: ")
    nome_curso = input("Digite o nome do curso: ")

    curso = None
    for obj in cursos:
        if obj.nome.lower() == nome_curso.lower():
            curso = obj

    if not curso:
        raise ValueError("Curso inválido.")

    aluno = None
    for obj in alunos:
        if obj.nome.lower() == nome_aluno.lower():
            aluno = obj

    if not aluno:
            raise ValueError("Aluno inválido.")

    curso.adicionar_aluno(aluno)
    print(f"Aluno {nome_aluno} cadastrado com sucesso no curso {nome_curso}.")

alunos = []
cursos = []
acao = 1
while acao != 0:
    print("Ações do sistema:")
    print("1 - Cadastrar aluno")
    print("2 - Cadastrar curso")
    print("3 - Cadastrar aluno em curso")
    print("4 - Visualizar cursos e seus alunos")
    acao = int(input("Escolha uma ação: "))

    match acao:
        case 1:
            while True:
                try:
                    aluno = cadastrarAluno()
                except ValueError as err:
                    print(err)
                    continue
                alunos.append(aluno)
                print("Aluno cadastrado com sucesso. \n")
                break
        case 2:
            nome = input("Digite o nome do curso: ")
            cursos.append(Curso(nome))
            print("Curso cadastrado com sucesso. \n")
            print('\n')
        case 3:
            while True:
                try:
                    cadastrarAlunoCurso()
                except ValueError as err:
                    print(err)
                    continue
                break
        case 4:
            for curso in cursos:
                print(f"Curso: {curso.nome}, Alunos:")
                curso.listar_alunos()
        case 0:
            print("Você está saindo do sistema.")
            break
        case _:
            print("Ação inválida.")
            continue