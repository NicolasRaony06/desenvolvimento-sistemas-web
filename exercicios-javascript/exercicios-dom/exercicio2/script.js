const numero = document.querySelector("#numero")
numero.textContent = 0

const aumentarBtn = document.querySelector("#aumentar")
const diminuirBtn = document.querySelector("#diminuir")

aumentarBtn.addEventListener('click', () => {
    numero.textContent++
})

diminuirBtn.addEventListener('click', () => {
    numero.textContent--
})