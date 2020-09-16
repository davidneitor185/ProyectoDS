class Servicio:
    def __init__(self, idServicio, cliente, factura, usuario, fechaDomicilio, tipo, estado):
        self.idServicio = idServicio
        self.cliente = cliente
        self.factura = factura
        self.usuario = usuario
        self.fechaDomicilio = fechaDomicilio
        self.tipo = tipo
        self.estado = estado