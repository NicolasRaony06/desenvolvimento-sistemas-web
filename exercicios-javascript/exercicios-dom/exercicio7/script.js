class Produto{
    constructor(nome, preco, quantidade){
        this.nome = nome
        this.preco = preco
        this.quantidade = quantidade
    }

    toHtml(classe = ''){
        return `
        <div class=${classe}>
        <h2>${this.nome}</h2>
        <p>${this.preco}</p>
        <p>${this.quantidade}</p>
        </div>
        `
    }
}


const produtos = [
    new Produto("Banana", 7.50, 18),
    new Produto("Café", 14.24, 79),
    new Produto("Arroz", 8.91, 94),
    new Produto("Macarrão", 5.80, 61),
    new Produto("Maçã", 6.20, 28),
    new Produto("Cereal", 9.60, 24),
    new Produto("Feijão", 10.70, 21)
]


const div = document.querySelector('div')
let html = ["<h1>Produtos:</h1>","<p>Para quantidades menores que 25</p>"]
produtos.forEach(produto => {
    console.log(produto.toHtml())
    if(produto.quantidade < 25){
        html.push(produto.toHtml('red'))
        return
    }
    html.push(produto.toHtml())
})

div.innerHTML = html.join('')