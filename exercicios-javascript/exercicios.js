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
    
}

/* questao1(3665)*/
// questao2(33)
// questao3(100, 1)
questao4(2000)