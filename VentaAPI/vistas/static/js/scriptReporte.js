const total = document.getElementById("num")

function bubbleSort(arr) {
    var i, j;
    var len = arr.length;

    var isSwapped = false;
    for (i = 0; i < len; i++) {
        isSwapped = false;
        for (j = 0; j < (len - i - 1); j++) {
            if (arr[j] > arr[j + 1]) {
                var temp = arr[j]
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
                isSwapped = true;
            }
        }
        if (!isSwapped) {
            break;
        }
    }
}

function obtenerTotalClientes() {
    let cant

    $.getJSON('http://127.0.0.1:8000/venta/obtener-todos-los-clientes', function (data) {
        var clientes = JSON.parse(data); // Convertir el objeto JSON en un array
        cant = clientes.length
    });

    total.innerText = total
}


function cargarCliente() {
    var divCancion = document.getElementById("canciones");
    var divDetalle = document.getElementById("detalles");
    var divMenu = document.getElementById("menu");

    $.getJSON('http://127.0.0.1:8000/venta/obtener-todos-los-clientes', function (data) {
        var clientes = JSON.parse(data); // Convertir el objeto JSON en un array
        console.log(clientes);
        // Recorrer la lista de clientes y crear las tarjetas
        clientes.forEach(function (cliente) {
            var cardHtml =
                `<div class="canciones">
                <div class="detalles">
                    <span>${cliente._nombre}</span>
                    <span>90%</span>
                </div>
                <div class="menu">
                    <div id="uno-menu"></div>
                </div>
            </div>`;
            $('#cardReportUser').append(cardHtml);
        });
    });
}

// function loadClientes() {

//     $.getJSON('http://127.0.0.1:8000/venta/obtener-todos-los-clientes', function (data) {
//         var clientes = JSON.parse(data); // Convertir el objeto JSON en un array
//         console.log(clientes);
//         // Recorrer la lista de clientes y crear las tarjetas
//         clientes.forEach(function (cliente) {
//             var cardHtml =
//                 `<div class="col-md-4">
//                 <div class="card">
//                     <div class="card-body">
//                         <h5 class="card-title">${cliente._nombre}</h5>
//                         <p class="card-text"><strong>NIT:</strong> ${cliente._nit}</p>
//                         <p class="card-text"><strong>Dirección:</strong> ${cliente._direccion}</p>
//                     </div>
//                 </div>
//             </div>`;
//             $('#clientes-container').append(cardHtml);
//         });
//     });
// }