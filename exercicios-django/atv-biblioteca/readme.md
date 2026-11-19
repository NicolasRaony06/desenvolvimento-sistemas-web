# Atividade Biblioteca Django

Uma atividade de Django para gerenciar uma biblioteca digital com autores, livros e categorias, aplicando conceitos de normalização de dados e relações entre modelos.

## 📋 Descrição

Esta atividade implementa um sistema de biblioteca que permite cadastrar livros, autores e categorias, com uma estrutura normalizada de banco de dados. O foco principal é a demonstração de:

- Relacionamentos entre modelos (ForeignKey, ManyToManyField)
- Configuração avançada do admin do Django
- Views e templates para exibição de dados
- Tratamento de erros 404
- Buscas e filtros no admin

## ✅ Conformidade com a Atividade

### 1. Modelos Normalizados

#### Model `Author`
- **Fields:**
  - `name` (CharField, obrigatório): Nome do autor
  - `nationality` (CharField, opcional): Nacionalidade do autor
- **Meta:**
  - Ordenação por nome
  - Nome plural definido como "Autores"
- **Método `__str__`:** Retorna o nome do autor

#### Model `Category`
- **Fields:**
  - `name` (CharField, único): Nome da categoria
- **Meta:**
  - Nome plural definido como "Categorias"
- **Método `__str__`:** Retorna o nome da categoria

#### Model `Book`
- **Fields:**
  - `tittle` (CharField): Título do livro
  - `author` (ForeignKey para Author): Relacionamento com autor
  - `published_year` (IntegerField): Ano de publicação
  - `available` (BooleanField): Disponibilidade do livro
  - `categories` (ManyToManyField para Category): Categorias do livro
- **Meta:**
  - Ordenação por título
  - Nome plural definido como "Livros"
- **Método `__str__`:** Retorna o título do livro

### 2. Respostas Atividade
#### 2.1 Justificativa do `on_delete=models.PROTECT`

**Decisão:** Utilizar `models.PROTECT` na ForeignKey de `author` em `Book` para evitar perda de dados de Livro. Assim, para excluir autor é preciso primeiro resolver as pendencias existentes, no caso seus livros. Ao tentar remover autor é retornado um erro `ProtectedError`.

#### 2.2 Explicação proteção django CRSF

Ao retirar a tag `{% crsf_token %}` do template, o middleware do django impede que a página seja renderizada, retornando um erro HTTP 403 Forbidden com a mensagem `CSRF verification failed. Request aborted.` ao tentar enviar o formulário via POST. Isso é uma medida de segurança, pois o backend não consegue validar a vericidade da requisação sem o token de proteção embutido no formulário.

#### 2.3.1 O LivroModelForm mudou? Por que as regras do Model funcionam nele e no Admin sem nenhuma alteração?

O LivroModelForm apenas mudou para adicionar os novos campos de Model Livro, entretanto em relação a adição dos validadores não houve mudança. Isso se dá, porque o ModelForm quando instancia o model, já chama todas as validações de cada campo.

#### 2.3.2 Qual é a diferença entre um validator e o método clean_<campo>()? Dê um exemplo de regra que só pode ser feita com clean_<campo>().

Um validator por ser usando globalmente por todo o sistema, difentemente do clean_campo, que apenas é utilizavel no ModelForm. O clean_campo permite alterar o valor de um campo e formatar no formato desejado na hora de salvar o Model.

#### 2.3.3 Para cada regra, diga qual estratégia usar: argumento do campo, validators=[...], clean_<campo>() ou clean(). Justifique. 
<ul>
  <li>
    O título não pode ser igual ao nome do autor.
    Resposta: clean(), pois é preciso validar dois campos do form, dessa forma, é mais correto utilizar um validação geral do form.
  </li>
  <li>
    O título deve ser salvo sem espaços no início e no fim.
    Resposta: validators, pois não há a intenção de formatar o campo, apenas checar e repassar o erro, impedindo que o campo seja salvo incorreto.
  </li>
  <li>
    O número de páginas deve ser no máximo 5000.
    Resposta: argumento do campo, nesse caso um max_lenght direto no campo do Model, já resolve de forma mais simples e direta a necessidade de validação.
  </li>
  <li>
    Um livro "indisponível" precisa ter o ISBN preenchido.
    Resposta: clean(), pois é preciso validar dois campos ao mesmo tempo.
  </li>
</ul>

#### 2.4.1 O que acontece se esquecermos request.FILES na view? E se esquecermos o enctype no template? Reproduza os dois erros e descreva o que viram (o formulário dá algum aviso?).

O ModelForm não irá conseguir ter acesso ao arquivo de imagem e salvar no servidor e no banco de dados como endereço. Esquecendo o enctype no template, o arquivo de imagem não será enviado para o backend, apenas o seu nome, que é passado pelo request.POST. Entretanto, em nenhum dos casos o formulário repassa o erro, a não ser que o campo de imagem esteja como obrigatório.

#### 2.4.2 Qual é a diferença entre STATICFILES_DIRS / {% static %} e MEDIA_ROOT / .url? Quando usar cada um na Mini biblioteca?

Os static files são os arquivos estáticos do servidor, sempre utilizados para renderização de imagem, css e javascript. Já o media, são arquivos enviados por usuários via upload. No contexto de uma Mini Biblioteca, se deve utilizar o static para arquivos como imagens não atreladas à um usuário e css/js, e já o media para arquivos como capa de um livro ou foto de perfil. 

#### 2.4.3 Ao excluir um livro (ou trocar a capa), o arquivo antigo continua em media/capas/. Por que isso acontece e que problema pode causar a longo prazo?

Sim, por padrão o django não faz o tratamento de arquivos atrelados a campos que foram excluídos. Isso pode gerar excesso de dados inúteis que levaram ao servidor de arquivos local ou remoto a exceder seu armazenamento com dados desnecessários.

#### 2.4.4 Por que a extensão do arquivo não basta como proteção? Que outros cuidados o servidor deve ter com uploads?

Porque usuarios mal intencionados conseguem ainda enviar arquivos que não são imagens, mas que têm a extensão de uma, como exemplo <code>malware.js.png</code>. Por isso o servidor deve validar o formato do arquivo abrindo ele e checando sua assinatura interna em bytes. Além disso, é válido limitar o tamanho do arquivo antes de ser salvo, e salvar num local externo ao diretório base do servidor.


### 3. Configuração do Admin

#### `BookAdmin`
```python
list_display = ['tittle', 'author', 'published_year', 'available']
list_filter = ['available', 'categories']
search_fields = ['tittle', 'author__name']
filter_horizontal = ['categories']
```
- **`list_display`:** Exibe título, autor, ano de publicação e disponibilidade
- **`list_filter`:** Filtra por disponibilidade e categoria
- **`search_fields`:** Busca por título e nome do autor (via `author__name`)
- **`filter_horizontal`:** Interface melhorada para selecionar múltiplas categorias

#### `AuthorAdmin`
```python
inlines = [BookInline]
```
- **`inlines`:** BookInline permite editar livros diretamente na página do autor
- Facilita a gestão de livros relacionados sem sair da página do autor

#### `CategoryAdmin`
- Registrado no admin para gerenciamento de categorias

### 4. Views e Templates

#### View `view_books` (Lista de livros)
- Exibe todos os livros com seus autores
- Nome do autor é um link para a página de detalhes do autor
- Usa `select_related('author')` para otimização de queries
- Renderiza `book/view.html`

#### View `view_author` (Detalhes do autor)
- Tratamento de erro 404 com `get_object_or_404`
- Lista todos os livros do autor usando `author.books.all()` (relacionamento reverso)
- Exibe informações do autor (nome e nacionalidade)
- Renderiza `author/view.html`

#### Template `book/view.html` (Lista de livros)
- Exibe tabela com todos os livros
- Nome do autor é um link para `/library/author/<id>/`
- Mostra título, autor, ano e disponibilidade

#### Template `author/view.html` (Detalhes do autor)
- Exibe informações do autor (nome, nacionalidade)
- Lista todos os livros do autor em tabela
- Mostra aviso se o autor não tiver livros

## 🚀 Como Executar

### 1. Configuração do Ambiente

```bash
# Instalar dependências
pip install -r requirements.txt

# Navegar para o diretório do projeto
cd atv-biblioteca

# Aplicar migrações
python manage.py migrate
```

### 2. Criar Superusuário (Admin)

```bash
python manage.py createsuperuser
```

### 3. Iniciar o Servidor

```bash
python manage.py runserver
```

### 4. Acessar a Aplicação

- **Home:** `http://127.0.0.1:8000/` (ou conforme configurado em `urls.py`)
- **Listar Livros:** `http://127.0.0.1:8000/library/books/`
- **Ver Autor:** `http://127.0.0.1:8000/library/author/<id>/`
- **Admin:** `http://127.0.0.1:8000/admin/`

## 📁 Estrutura do Projeto

```
atv-biblioteca/
├── manage.py
├── db.sqlite3
├── README.md (este arquivo)
├── requirements.txt
├── core/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   ├── wsgi.py
│   └── __pycache__/
├── library/
│   ├── migrations/
│   ├── templates/
│   │   ├── book/
│   │   │   ├── register.html (cadastro de livros)
│   │   │   └── view.html (listagem de livros)
│   │   └── author/
│   │       └── view.html (detalhes do autor)
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   └── __pycache__/
└── templates/
    └── base.html
```

## 🔧 Tecnologias Utilizadas

- **Django 3.x/4.x:** Framework web Python
- **SQLite:** Banco de dados padrão (pode ser alterado em `settings.py`)
- **HTML/CSS:** Renderização frontend
- **Python 3.8+:** Linguagem de programação

## 📝 URLs Disponíveis

As URLs são configuradas em `library/urls.py`:

| Rota | View | Template | Descrição |
|------|------|----------|-----------|
| `/library/books/` | `view_books` | `book/view.html` | Lista todos os livros |
| `/library/author/<id>/` | `view_author` | `author/view.html` | Exibe detalhes de um autor e seus livros |
| `/library/register/` | `register_book` | `book/register.html` | Cadastra novo livro |

## 🎯 Funcionalidades Implementadas

- ✅ Cadastro e listagem de livros
- ✅ Cadastro e listagem de autores
- ✅ Gerenciamento de categorias
- ✅ Admin do Django com buscas e filtros avançados
- ✅ Relacionamentos normalizados (ForeignKey e ManyToManyField)
- ✅ Links entre livros e autores
- ✅ Tratamento de erros 404 com `get_object_or_404`
- ✅ Interface inline para editar livros na página do autor
- ✅ Otimização de queries com `select_related()`
- ✅ Proteção referencial com `on_delete=models.PROTECT`

## 📌 Notas Importantes

1. **ManyToManyField opcional:** Um livro pode não ter categorias atribuídas (o campo é opcional).

2. **Busca no Admin:** A busca funciona tanto pelo título do livro quanto pelo nome do autor através do campo `author__name`.

3. **Select Related:** A view de livros usa `select_related('author')` para otimizar queries ao banco de dados, reduzindo o número de consultas.

4. **Related Name:** O `related_name="books"` em `Book.author` permite acessar os livros de um autor via `author.books.all()` no template.

## 🐛 Tratamento de Erros

- **Autor não existe:** Ao acessar `/library/author/<id>/` com um ID inválido, retorna erro 404 (página não encontrada).
- **Autor com livros:** Ao tentar deletar um autor com livros associados pelo admin, retorna `ProtectedError` informando que a operação não é permitida.
- **Categoria em uso:** As categorias podem ser deletadas do admin, pois `ManyToManyField` não usa `on_delete`.

## 🔄 Fluxo de Dados

```
1. Usuário acessa /library/books/
   ↓
2. View view_books() busca todos os Book com select_related('author')
   ↓
3. Template book/view.html renderiza lista com links para autores
   ↓
4. Usuário clica no nome do autor
   ↓
5. View view_author(id) busca Author por ID (404 se não encontrar)
   ↓
6. Template author/view.html renderiza dados do autor e seus livros
   ↓
7. Livros exibidos via relacionamento reverso author.books.all()
```

## 📚 Conceitos Django Aplicados

- **ForeignKey:** Relacionamento 1-para-muitos (Author → Book)
- **ManyToManyField:** Relacionamento muitos-para-muitos (Book ↔ Category)
- **Admin Inline:** Edição de modelos relacionados em uma única página
- **Filter Horizontal:** Interface melhorada para seleção de ManyToMany
- **Meta Options:** Definição de ordenação, nomes plural e verbose_name
- **Related Names:** Acesso reverso aos relacionamentos
- **Query Optimization:** Uso de `select_related()` para evitar N+1 queries
- **Error Handling:** Uso de `get_object_or_404()` para tratamento de erros

