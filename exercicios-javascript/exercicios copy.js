/**
 * Escreva um programa que, a partir de uma duração em segundos, calcule e exiba a quantas horas, minutos e segundos ela equivale (ex.: 3665 → 1h 1min 5s).
 * @param {number} segundos 
 */
function questao1(segundos){
    let horas, minutos
    horas = Math.trunc(segundos / 3600)

    minutos = Math.trunc(Math.trunc(segundos % 3600) / 60)

    console.log(`Hora: ${horas}, Minuto: ${minutos}, Segundo: ${Math.trunc(segundos % 3600) % 60}`)
}

/**
 * Dada uma temperatura em Celsius, calcule e exiba o equivalente em Fahrenheit e em Kelvin.
 * @param {number} celsius 
 */
function questao2(celsius){
    console.log(`Fahrenheit: ${((celsius * 1.8) + 32)}, Kelvin: ${celsius + 273.15}`)
}

/**
 *  Escreva um programa que recebe o preço de um produto e a quantidade comprada, calcula o subtotal, aplica um desconto progressivo (5% acima de R$100, 10% acima de R$300) e exibe um resumo formatado do pedido usando template literals.
 * @param {number} preco 
 * @param {number} quantidade 
 */
function questao3(preco, quantidade) {
    let subtotal = preco * quantidade 
    if (subtotal > 100 && subtotal <= 300){
        console.log(`Pedido: preço = ${preco}, quantidade = ${quantidade}, subtotal = ${subtotal * 0.95}`)
        return
    }
    else if (subtotal > 300 ){
        console.log(`Pedido: preço = ${preco}, quantidade = ${quantidade}, subtotal = ${subtotal * 0.90}`)
        return
    }
    console.log(`Pedido: preço = ${preco}, quantidade = ${quantidade}, subtotal = ${subtotal}`)

}

/**
 *  Dado o ano de nascimento de uma pessoa, calcule a idade e determine, combinando operadores lógicos e de comparação, se ela já pode votar, se o voto é obrigatório e se ela ainda está isenta do serviço militar.
 * @param {number} ano_nascimento 
 */
function questao4(ano_nascimento){
    const ano_atual = new Date().getFullYear()
    let idade = ano_atual - ano_nascimento
    let podeVotar = false
    let obgVotar = false
    let servMilitarIsento = false

    if(idade >= 18){
        podeVotar = true
        obgVotar = true
    }
    else if(idade >= 16 && idade < 18){
        podeVotar = true
        servMilitarIsento = true
    }
    else {
        servMilitarIsento = true
    }

    console.log(idade, podeVotar, obgVotar, servMilitarIsento);
}

/**
 * 5. Calculadora usando switch/case.
 * @param {number} numero1
 * @param {number} numero2
 * @param {string} operador
 * @returns {number|string}
 */
function questao5(numero1, numero2, operador) {
    switch (operador) {
        case '+':
            return numero1 + numero2
        case '-':
            return numero1 - numero2
        case '*':
            return numero1 * numero2
        case '/':
            if (numero2 === 0) {
                return "Erro: divisão por zero"
            }
            return numero1 / numero2
        default:
            return "Erro: operador inválido"
    }
}

/**
 * 6. Calcula a classificação do IMC.
 * @param {number} peso
 * @param {number} altura
 * @returns {string}
 */
function questao6(peso, altura) {
    const imc = peso / (altura * altura)

    if (imc < 18.5) {
        return "Abaixo do peso"
    }
    else if (imc < 25) {
        return "Normal"
    }
    else if (imc < 30) {
        return "Sobrepeso"
    }
    else {
        return "Obesidade"
    }
}

/**
 * 7. Pedra, Papel e Tesoura.
 * @param {string} jogador1
 * @param {string} jogador2
 * @returns {string}
 */
function questao7(jogador1, jogador2) {
    if (jogador1 === jogador2) {
        return "Empate"
    }

    const vence = {
        pedra: "tesoura",
        papel: "pedra",
        tesoura: "papel"
    }

    if (vence[jogador1] === jogador2) {
        return "Jogador 1 venceu"
    }

    if (vence[jogador2] === jogador1) {
        return "Jogador 2 venceu"
    }

    return "Jogada inválida"
}

/**
 * 8. Verifica se uma string é um palíndromo, ignorando maiúsculas/minúsculas e espaços.
 * @param {string} texto
 * @returns {boolean}
 */
function questao8(texto) {
    const textoFormatado = texto.toLowerCase().replace(/\s/g, "")
    const textoInvertido = textoFormatado.split("").reverse().join("")

    return textoFormatado === textoInvertido
}

/**
 * 9. Retorna a média, a maior e a menor nota de um array.
 * @param {number[]} notas
 * @returns {{media: number, maior: number, menor: number}}
 */
function questao9(notas) {
    const soma = notas.reduce((total, nota) => total + nota, 0)

    return {
        media: soma / notas.length,
        maior: Math.max(...notas),
        menor: Math.min(...notas)
    }
}

/**
 * 10. Calcula o n-ésimo termo da sequência de Fibonacci.
 * Considera Fibonacci(0) = 0 e Fibonacci(1) = 1.
 * @param {number} n
 * @returns {number}
 */
function questao10(n) {
    if (n < 0) {
        return "Erro: n deve ser maior ou igual a 0"
    }

    let anterior = 0
    let atual = 1

    for (let i = 0; i < n; i++) {
        let proximo = anterior + atual
        anterior = atual
        atual = proximo
    }

    return anterior
}

/**
 * 11. Validação de senha.
 * @param {string} senha
 * @returns {string[]}
 */
function questao11(senha) {
    const regrasNaoCumpridas = []

    if (senha.length < 8) {
        regrasNaoCumpridas.push("Mínimo de 8 caracteres")
    }

    if (!/[A-Z]/.test(senha)) {
        regrasNaoCumpridas.push("Ao menos uma letra maiúscula")
    }

    if (!/[0-9]/.test(senha)) {
        regrasNaoCumpridas.push("Ao menos um número")
    }

    return regrasNaoCumpridas
}

/**
 * 12. Operações sobre produtos em estoque.
 * @param {{nome: string, preco: number, quantidade: number}[]} produtos
 * @returns {number}
 */
function valorTotalEstoque(produtos) {
    return produtos.reduce(
        (total, produto) => total + (produto.preco * produto.quantidade),
        0
    )
}

/**
 * 12. Encontra o produto mais caro.
 * @param {{nome: string, preco: number, quantidade: number}[]} produtos
 * @returns {{nome: string, preco: number, quantidade: number}}
 */
function produtoMaisCaro(produtos) {
    return produtos.reduce((maisCaro, produto) =>
        produto.preco > maisCaro.preco ? produto : maisCaro
    )
}

/**
 * 12. Lista os produtos cuja quantidade está abaixo do mínimo informado.
 * @param {{nome: string, preco: number, quantidade: number}[]} produtos
 * @param {number} minimo
 * @returns {{nome: string, preco: number, quantidade: number}[]}
 */
function produtosAbaixoDoMinimo(produtos, minimo) {
    return produtos.filter(produto => produto.quantidade < minimo)
}

/**
 * 13. Agenda de contatos.
 * @param {{nome: string, telefone: string, categoria: string}[]} contatos
 */
function adicionarContato(contatos, nome, telefone, categoria) {
    contatos.push({
        nome: nome,
        telefone: telefone,
        categoria: categoria
    })
}

/**
 * 13. Remove um contato pelo nome.
 * @param {{nome: string, telefone: string, categoria: string}[]} contatos
 */
function removerContato(contatos, nome) {
    const indice = contatos.findIndex(contato =>
        contato.nome.toLowerCase() === nome.toLowerCase()
    )

    if (indice !== -1) {
        contatos.splice(indice, 1)
    }
}

/**
 * 13. Lista os contatos de uma categoria.
 * @param {{nome: string, telefone: string, categoria: string}[]} contatos
 * @returns {{nome: string, telefone: string, categoria: string}[]}
 */
function listarContatosPorCategoria(contatos, categoria) {
    return contatos.filter(contato =>
        contato.categoria.toLowerCase() === categoria.toLowerCase()
    )
}

/**
 * 13. Retorna um novo array contendo apenas os valores únicos.
 * @param {any[]} numeros
 * @returns {any[]}
 */
function valoresUnicos(numeros) {
    return [...new Set(numeros)]
}

/**
 * 14. Classe Produto.
 */
class Produto {
    constructor(nome, preco, quantidade) {
        this.nome = nome
        this.preco = preco
        this.quantidade = quantidade
    }

    aplicarDesconto(percentual) {
        this.preco = this.preco * (1 - percentual / 100)
    }

    estaDisponivel() {
        return this.quantidade > 0
    }
}

/**
 * 15. Classe ContaBancaria.
 */
class ContaBancaria {
    constructor(titular, saldo = 0) {
        this.titular = titular
        this.saldo = saldo
    }

    depositar(valor) {
        if (valor <= 0) {
            return "Erro: o valor do depósito deve ser positivo"
        }

        this.saldo += valor
        return `Depósito de R$ ${valor.toFixed(2)} realizado`
    }

    sacar(valor) {
        if (valor <= 0) {
            return "Erro: o valor do saque deve ser positivo"
        }

        if (valor > this.saldo) {
            return "Erro: saldo insuficiente"
        }

        this.saldo -= valor
        return `Saque de R$ ${valor.toFixed(2)} realizado`
    }

    extrato() {
        return `Titular: ${this.titular} | Saldo: R$ ${this.saldo.toFixed(2)}`
    }
}

/**
 * 16. Classe Retangulo.
 */
class Retangulo {
    constructor(base, altura) {
        this.base = base
        this.altura = altura
    }

    calcularArea() {
        return this.base * this.altura
    }

    calcularPerimetro() {
        return 2 * (this.base + this.altura)
    }
}

/**
 * 17. Reescrita do exercício de estoque usando uma classe.
 * Os dados são propriedades de instância e as operações são métodos.
 */
class Estoque {
    constructor(produtos = []) {
        this.produtos = produtos
    }

    adicionarProduto(nome, preco, quantidade) {
        this.produtos.push({
            nome: nome,
            preco: preco,
            quantidade: quantidade
        })
    }

    valorTotal() {
        return this.produtos.reduce(
            (total, produto) => total + produto.preco * produto.quantidade,
            0
        )
    }

    produtoMaisCaro() {
        return this.produtos.reduce((maisCaro, produto) =>
            produto.preco > maisCaro.preco ? produto : maisCaro
        )
    }

    produtosAbaixoDoMinimo(minimo) {
        return this.produtos.filter(produto => produto.quantidade < minimo)
    }
}

// questao1(3665)
// questao2(33)
// questao3(100, 1)
// questao4(2000)

// console.log(questao5(10, 5, '+'))
// console.log(questao5(10, 0, '/'))
// console.log(questao5(10, 5, '%'))

// console.log(questao6(70, 1.75))

// console.log(questao7("pedra", "tesoura"))
// console.log(questao8("A base do teto desaba"))
// console.log(questao9([7, 8, 9, 10]))
// console.log(questao10(10))
// console.log(questao11("Senha123"))

// const produtos = [
//     {nome: "Notebook", preco: 3000, quantidade: 5},
//     {nome: "Mouse", preco: 80, quantidade: 2},
//     {nome: "Teclado", preco: 150, quantidade: 10}
// ]

// console.log(valorTotalEstoque(produtos))
// console.log(produtoMaisCaro(produtos))
// console.log(produtosAbaixoDoMinimo(produtos, 5))

// const contatos = []

// adicionarContato(contatos, "Nicolas", "99999-9999", "Amigos")
// adicionarContato(contatos, "Álvaro", "98888-8888", "Faculdade")
// adicionarContato(contatos, "Keven", "97777-7777", "Amigos")

// console.log(listarContatosPorCategoria(contatos, "Amigos"))
// removerContato(contatos, "Álvaro")
// console.log(contatos)

// console.log(valoresUnicos([1, 2, 2, 3, 4, 4, 5]))

// const produto1 = new Produto("Notebook", 3000, 5)
// const produto2 = new Produto("Mouse", 100, 0)
// const produto3 = new Produto("Teclado", 200, 10)

// produto1.aplicarDesconto(10)

// console.log(produto1)
// console.log(produto1.estaDisponivel())
// console.log(produto2.estaDisponivel())
// console.log(produto3.estaDisponivel())

// const conta1 = new ContaBancaria("Nicolas", 1000)
// const conta2 = new ContaBancaria("Álvaro", 500)

// console.log(conta1.depositar(200))
// console.log(conta1.sacar(150))
// console.log(conta1.sacar(2000))

// console.log(conta1.extrato())
// console.log(conta2.extrato())

// const retangulo = new Retangulo(10, 5)

// console.log(retangulo.calcularArea())
// console.log(retangulo.calcularPerimetro())

// const estoque = new Estoque([
//     {nome: "Notebook", preco: 3000, quantidade: 5},
//     {nome: "Mouse", preco: 80, quantidade: 2},
//     {nome: "Teclado", preco: 150, quantidade: 10}
// ])

// console.log(estoque.valorTotal())
// console.log(estoque.produtoMaisCaro())
// console.log(estoque.produtosAbaixoDoMinimo(5))
