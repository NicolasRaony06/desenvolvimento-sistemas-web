const form = document.querySelector('form')
const div = document.querySelector('div')

form.addEventListener('submit', (e) => {
    e.preventDefault()

    const peso = document.querySelector("#peso")
    const altura = document.querySelector("#altura")

    peso.value = (peso.value).replace(",", ".")
    altura.value = (altura.value).replace(",", ".")
    
    let imc = peso.value / (altura.value**2)
    let classificação = ''
    if(imc < 18.5){
        classificação = "Abaixo do peso"
    }
    else if(imc <= 24.9){
        classificação = "Peso adequado"
    }
    else if(imc <= 29.9){
        classificação = "Sobrepeso"
    }
    else if(imc <= 34.9){
        classificação = "Obesidade grau I"
    } 
    else if(imc <= 39.9){
        classificação = "Obesidade grau II"
    }
    else { classificação = "Obesidade grau III"}
    
    let html = `<h2>Classificação: ${classificação}</h2 >
    <h3>IMC: ${imc.toFixed(2)}</h3>`

    div.innerHTML = html
})