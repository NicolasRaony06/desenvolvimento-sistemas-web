const lista = document.querySelectorAll("#lista li")

lista.forEach(li => {
    if((li.textContent).length > 100){
        li.classList.add("red")
    }
})