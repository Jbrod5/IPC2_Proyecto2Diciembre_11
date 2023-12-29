function agregarProducto() {
    var divProductos = document.getElementById("productos");
    var nuevoProducto = document.createElement("div");
    nuevoProducto.className = "form-row";
    nuevoProducto.innerHTML = 
        `<br>
        <div class="col">
            <input type="text" class="form-control" name="codigo[]" placeholder="Codigo del producto">
        </div>
        <div class="col">
            <input type="text" class="form-control" name="cantidad[]" placeholder="Cantidad">
        </div>
        <div class="col-auto">
            <button type="button" class="submitButton" onclick="eliminarProducto(this)">Eliminar</button>
        </div>`;
    divProductos.appendChild(nuevoProducto);
}

function eliminarProducto(elemento) {
    var divProductos = document.getElementById("productos");
    divProductos.removeChild(elemento.parentNode.parentNode);
}

function agregarFactura() {
    var divContenido = document.getElementById("contenido");
    var vistaExistente = document.querySelector(".form-factura");

    if (!vistaExistente) {
        var vista = document.createElement("div");
        vista.className = "form-factura";
        vista.innerHTML =
            `<div class="container">
                <form action="http://127.0.0.1:8000/venta/ingresar-factura" method="POST">
                    <div class="titulo">
                        <input type="text" class="form-control" id="nit" name="nit" placeholder="NIT">
                    </div>

                    <div id="productos">
                        <div class="form">
                            <div class="col">
                                <input type="text" class="form-control" name="codigo[]" placeholder="Codigo del producto">
                            </div>
                            <div class="col">
                                <input type="text" class="form-control" name="cantidad[]" placeholder="Cantidad">
                            </div>
                            <div class="col-auto">
                                <button type="button" class="submitButton" onclick="eliminarProducto(this)">Eliminar</button>
                            </div>
                        </div>
                    </div>
                    <button type="button" class="buttonForm" id="addProducto" onclick="agregarProducto()">Agregar Producto</button>
                    <br>
                    <input type="submit" class="buttonForm" id="guardar" value="Guardar Factura">
                </form>
                <script src="../JS/scriptsFacturas.js"></script>
            </div>`
        divContenido.appendChild(vista)
    }
}

function verFacturas() {
    var divContenido = document.getElementById("contenido");
    var vistaExistente = document.querySelector(".form-factura");

    if (vistaExistente) {
        divContenido.removeChild(vistaExistente);
        
    }

    if(!vistaExistente) {
        $.getJSON('http://127.0.0.1:8000/venta/obtener-todas-las-facturas', function(data) {
        var facturas = JSON.parse(data); // Convertir el objeto JSON en un array
        console.log(facturas);
        // Recorrer la lista de clientes y crear las tarjetas
        facturas.forEach(function(factura) {
            var cardHtml = 
                `<div class="cardProducto">
                    <h3 class="card-title"><strong>Producto:</strong> ${factura.noFactura}</h5>
                    <p class="card-text"><strong>Codigo:</strong> ${factura.obtener_ListaProductosComprados}</p>
                    
                </div>`;
                $('#contenido').append(cardHtml);
            });
        });
    }

    
}