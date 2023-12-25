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
            <button type="button" class="btn btn-danger" onclick="eliminarCampo(this)">Eliminar</button>
        </div>`;
    divProductos.appendChild(nuevoProducto);
}

function eliminarProducto(elemento) {
    var divProductos = document.getElementById("productos");
    divProductos.removeChild(elemento.parentNode.parentNode);
}