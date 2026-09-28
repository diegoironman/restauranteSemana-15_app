class Venta:
    def __init__(
        self,
        identificador: str,
        usuario_id: str,
        producto_codigo: str,
        fecha: str
    ) -> None:
        self.identificador = identificador.strip()
        self.usuario_id = usuario_id.strip()
        self.producto_codigo = producto_codigo.strip()
        self.fecha = fecha.strip()

        if not self.identificador:
            raise ValueError("El identificador de la venta no puede estar vacío.")

        if not self.usuario_id:
            raise ValueError("El usuario no puede estar vacío.")

        if not self.producto_codigo:
            raise ValueError("El producto no puede estar vacío.")

        if not self.fecha:
            raise ValueError("La fecha no puede estar vacía.")

    def convertir_a_diccionario(self) -> dict:
        return {
            "identificador": self.identificador,
            "usuario_id": self.usuario_id,
            "producto_codigo": self.producto_codigo,
            "fecha": self.fecha,
        }

    def __str__(self) -> str:
        return (
            f"{self.identificador} - "
            f"Usuario: {self.usuario_id} - "
            f"Producto: {self.producto_codigo} - "
            f"Fecha: {self.fecha}"
        )