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
                    <label for="codigo">Codigo:</label>
                    <input type="text" class="form-control" id="codigo" name="codigo" required>
                </div>
                <div class="form-group">
                    <label for="nombre">Nombre:</label>
                    <input type="text" class="form-control" id="nombre" name="nombre" required>
                </div>
                <div class="form-group">
                    <label for="descripcion">Descripcion:</label>
                    <input type="text" class="form-control" id="descripcion" name="descripcion" required>
                </div>
                <div class="form-group">
                    <label for="precio">Precio:</label>
                    <input type="text" class="form-control" id="precio" name="precio" required>
                </div>
                <div class="form-group">
                    <label for="stock">Stock:</label>
                    <input type="text" class="form-control" id="stock" name="stock" required>
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
        $.getJSON('http://127.0.0.1:8000/venta/obtener-todos-los-productos', function(data) {
        var productos = JSON.parse(data); // Convertir el objeto JSON en un array
        console.log(productos);
        // Recorrer la lista de clientes y crear las tarjetas
        productos.forEach(function(producto) {
            var cardHtml = 
                `<div class="cardProducto">
                    <h3 class="card-title"><strong>Producto:</strong> ${producto._nombre}</h5>
                    <p class="card-text"><strong>Codigo:</strong> ${producto._codigo}</p>
                    <p class="card-text"><strong>Descripcion:</strong> ${producto._descripcion}</p>
                    <p class="card-text"><strong>Precio:</strong> ${producto._precio}</p>
                    
                </div>`;
                $('#producto-container').append(cardHtml);
            });
        });
    }
    
}