function confimarEliminacionfila(idfila) {


  window.location.href = "/ATodoGasApp/borrar_producto/" + idfila + "/";
  Swal.fire({      
      icon: 'info',
      title: 'El producto ha sido eliminado con exito',
      showConfirmButton: false,
      timer: 2000
    }
  )


}
