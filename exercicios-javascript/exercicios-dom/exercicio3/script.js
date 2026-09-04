const itens = document.querySelector("#itens")

itens.addEventListener('click', (e) => {
    if(e.target.tagName === 'LI'){
        e.target.classList.toggle('concluido')
    }
})