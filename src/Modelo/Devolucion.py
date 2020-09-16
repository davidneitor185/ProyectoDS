class Devolucion:
    def __init__(self, codigoEspDev, usuario, numeroFactura, codigoProductos, devolucionDeDinero, fechaDev):
        self.codigoEspDev = codigoEspDev
        self.usuario = usuario
        self.numeroFactura = numeroFactura
        self.codigoProductos = []
        self.devolucionDeDinero = devolucionDeDinero
        self.fechaDev = fechaDev