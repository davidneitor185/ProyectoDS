function confimarEliminacion(id){
    Swal.fire({
        title: '¿Está Seguro?',
        text: "No se podra recuperar el cliente!",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Si, Borrar!'
      }).then((result) => {
        if (result.isConfirmed) {
            window.location.href = "/ATodoGasApp/eliminar_cliente/"+id+"/";
          Swal.fire(
            'Borrado!',
            'El cliente se ha Eliminado.',
            'Completado'
          )
        }
      })
}
