const form = document.querySelector('form')
const div = document.querySelector('div')
form.addEventListener('submit', (e) => {
    e.preventDefault()

    const nome = document.querySelector("#nome")
    const idade = document.querySelector("#idade")
    const email = document.querySelector("#email")

    if(!((nome.value).length > 0 && (idade.value).length > 0 && (email.value).length > 0)){
        alert("Todos os campos precisam estar preenchidos!")
        return
    }
    if(idade.value < 1){
        alert("Idade deve ser superior a 0!")
        return
    }

    let html = `<h2>Nome: ${nome.value}</h2>
    <p>Email: ${email.value}</p>
    <p>Idade: ${idade.value}</p>`

    div.innerHTML = html
})