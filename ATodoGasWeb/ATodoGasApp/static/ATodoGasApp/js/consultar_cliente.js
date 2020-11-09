function consultar_cliente(){
    var id_cliente = document.getElementById("id_cliente");
    window.location.href = "/ATodoGasApp/consultar_cliente/"+id_cliente+"/";
    
    Swal.fire(
      id_cliente
    )
}
