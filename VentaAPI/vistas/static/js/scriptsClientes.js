function cargarClientes() {
    var divContenido = document.getElementById("clientes-container");
    var vistaExistente = document.querySelector(".cardClientes");
    var vistaCrearCliente = document.querySelector(".form-cliente");

    if(vistaCrearCliente) {
        divContenido.removeChild(vistaCrearCliente);
    }

    if (!vistaExistente) {
        $.getJSON('http://127.0.0.1:8000/venta/obtener-todos-los-clientes', function(data) {
        var clientes = JSON.parse(data); // Convertir el objeto JSON en un array
        console.log(clientes);
        // Recorrer la lista de clientes y crear las tarjetas
        clientes.forEach(function(cliente) {
            var cardHtml = 
                `<div class="cardClientes">
                    <h3 class="card-title">${cliente._nombre}</h5>
                    <p class="card-text"><strong>NIT:</strong> ${cliente._nit}</p>
                    <p class="card-text"><strong>Dirección:</strong> ${cliente._direccion}</p>                    
                </div>`;
                $('#clientes-container').append(cardHtml);
            });
        });
    }
}

function crearCliente() {
    var divContenido = document.getElementById("clientes-container");
    var vistaExistente = document.querySelector(".form-cliente");
    while (divContenido.firstChild) {
        divContenido.removeChild(divContenido.firstChild);
    }

    if (!vistaExistente) {
        var vista = document.createElement("div");
        vista.className = "form-cliente";
        vista.innerHTML =
            `<div class espacio-form>
            <form method="post" action="http://127.0.0.1:8000/venta/ingresar-cliente">
                <div class="form-group">
                    <label for="nit">NIT:</label>
                    <input type="text" class="form-control" id="nit" name="nit" required>
                </div>
                <div class="form-group">
                    <label for="nombre">Nombre:</label>
                    <input type="text" class="form-control" id="nombre" name="nombre" required>
                </div>
                <div class="form-group">
                    <label for="direccion">Dirección:</label>
                    <input type="text" class="form-control" id="direccion" name="direccion" required>
                </div>
                <button type="submit" class="submitButton">Enviar</button>
            </form>`
        divContenido.appendChild(vista)
    }
}
