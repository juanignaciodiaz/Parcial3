const url = 'https://mindicador.cl/api/dolar'
    fetch(url)
        .then(response => response.json())
        .then(data => {
            let element = document.getElementById('cambioDivisa')
            element.innerHTML = ` 
        <p>${data.nombre}</p>
        <p>${data.serie[0].valor}</p>`
            console.log(data)
        })
        .catch(err => console.log(err))


    setInterval(function () { mostrarhora() }, 1000);