const temaBtn = document.querySelector("#alterarTema")

temaBtn.addEventListener('click', () => {
    document.body.classList.toggle("dark")

    if(document.body.classList.contains('dark')){
        temaBtn.querySelector('span').textContent = "Escuro"
        return
    }
    temaBtn.querySelector('span').textContent = "Claro"
})