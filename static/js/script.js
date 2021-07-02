(function (d, w) {
    
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

    function mostrarhora(){
        let momentoActual = new Date();
        let hora = momentoActual.getHours();
        let minuto = momentoActual.getMinutes();
        let segundo = momentoActual.getSeconds();
    
        let horaImprimible = hora + ":" + minuto + ":" + segundo;
    
        const contenido_hora = document.getElementById('mostrarhora');
        contenido_hora.innerText = horaImprimible ;
    }
}) (document, window);