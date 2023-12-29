function crearProducto() {
    var divContenido = document.getElementById("producto-container");
    var vistaExistente = document.querySelector(".form-producto");
    while (divContenido.firstChild) {
        divContenido.removeChild(divContenido.firstChild);
    }

    if (!vistaExistente) {
        var vista = document.createElement("div");
        vista.className = "form-producto";
        vista.innerHTML =
            `<div class espacio-form>
            <form method="post" action="http://127.0.0.1:8000/venta/ingresar-producto">
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

function cargarProductos() {
    var divContenido = document.getElementById("producto-container");
    var vistaExistente = document.querySelector(".cardProducto");
    var vistaCrearProducto = document.querySelector(".form-producto");

    if(vistaCrearProducto) {
        divContenido.removeChild(vistaCrearProducto);
    }

    if (!vistaExistente) {
        $.getJSON('http://127.0.0.1:8000/venta/obtener-todas-los-productos', function(data) {
        var productos = JSON.parse(data); // Convertir el objeto JSON en un array
        console.log(clientes);
        // Recorrer la lista de clientes y crear las tarjetas
        productos.forEach(function(producto) {
            var cardHtml = 
                `<div class="cardProducto">
                    <h3 class="card-title">${producto._nombre}</h5>
                    <p class="card-text"><strong>NIT:</strong> ${producto._codigo}</p>
                    <p class="card-text"><strong>Dirección:</strong> ${cliente._descripcion}</p>
                    <p class="card-text"><strong>Dirección:</strong> ${cliente._precio}</p>
                    
                    <div class="dropdown">
                        <button class="dropbtn">Dropdown</button>
                            <div class="dropdown-content">
                                <a href="#">Ver Mas</a>
                                <a href="#">Editar</a>
                                <a href="#">Eliminar</a>
                            </div>
                        </div>
                </div>`;
                $('#producto-container').append(cardHtml);
            });
        });
    }
    
}