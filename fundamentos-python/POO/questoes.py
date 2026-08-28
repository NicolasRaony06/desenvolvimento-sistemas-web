class Pessoa:
    def __init__(self, nome : str, idade : int, email : str):
        if idade < 0:
            raise ValueError("A idade não pode ser negativa.")
        self.nome = nome
        self.idade = idade
        self.email = email

    def info(self):
        return f"Nome: {self.nome}, Idade: {self.idade}, E-mail: {self.email}"

    def aniversario(self):
        self.idade += 1

class Aluno(Pessoa):
    def __init__(self, nome : str, idade : int, email : str, matricula : int):
        super().__init__(nome, idade, email)
        self.matricula = matricula
        self.curso = None

    def exibir_dados_aluno(self):
        return self.info() + f"Matrícula: {self.matricula}, Curso: {self.curso}"

class Curso:
    def __init__(self, nome : str):
        self.nome = nome 
        self.alunos = []

    def adicionar_aluno(self, aluno : Aluno):
        if not isinstance(aluno, Aluno):
            raise ValueError("Aluno inválido.")

        self.alunos.append(aluno)
        aluno.curso = self.nome

    def listar_alunos(self):
        for i in self.alunos:
            print(i.exibir_dados_aluno())

#teste questão 1
if __name__ == "__main__":
    pessoa1 = Pessoa('José', 36, "josé@g.com")
    pessoa2 = Pessoa('Roberto', 25, "roberto@g.com")
    pessoa3 = Pessoa('Carol', 17, "carol@g.com")

    print(pessoa1.info())
    print(pessoa2.info())
    print(pessoa3.info())