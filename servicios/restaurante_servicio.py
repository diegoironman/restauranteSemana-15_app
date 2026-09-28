from datetime import date

from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta


class RestauranteServicio:
    def __init__(self, archivo_servicio) -> None:
        self.archivo_servicio = archivo_servicio
        self.productos = []
        self.usuarios = []
        self.ventas = []

        self._cargar_datos()

    def _cargar_datos(self) -> None:
        datos_productos = self.archivo_servicio.cargar_productos()
        datos_usuarios = self.archivo_servicio.cargar_usuarios()
        datos_ventas = self.archivo_servicio.cargar_ventas()

        self.productos = [
            Producto(
                item["codigo"],
                item["nombre"],
                item["categoria"],
                float(item["precio"]),
                int(item["stock"])
            )
            for item in datos_productos
        ]

        self.usuarios = [
            Usuario(
                item["usuario"],
                item["nombre"],
                item["contrasena"]
            )
            for item in datos_usuarios
        ]

        self.ventas = [
            Venta(
                item["identificador"],
                item["usuario_id"],
                item["producto_codigo"],
                item["fecha"]
            )
            for item in datos_ventas
        ]

    def _guardar_productos(self) -> None:
        productos_json = [
            {
                "codigo": producto.codigo,
                "nombre": producto.nombre,
                "categoria": producto.categoria,
                "precio": producto.precio,
                "stock": producto.stock
            }
            for producto in self.productos
        ]

        self.archivo_servicio.guardar_productos(productos_json)

    def _guardar_ventas(self) -> None:
        ventas_json = [
            venta.convertir_a_diccionario()
            for venta in self.ventas
        ]

        self.archivo_servicio.guardar_ventas(ventas_json)

    def _validar_datos_producto(
        self,
        codigo: str,
        nombre: str,
        categoria: str,
        precio: str,
        stock: str
    ) -> tuple[bool, str, float | None, int | None]:

        if not codigo or not nombre or not categoria:
            return (
                False,
                "Código, nombre y categoría son obligatorios.",
                None,
                None
            )

        try:
            precio_numero = float(precio)
            stock_numero = int(stock)
        except ValueError:
            return (
                False,
                "El precio debe ser numérico y el stock un número entero.",
                None,
                None
            )

        if precio_numero < 0:
            return False, "El precio no puede ser negativo.", None, None

        if stock_numero < 0:
            return False, "El stock no puede ser negativo.", None, None

        return True, "", precio_numero, stock_numero

    def validar_acceso(self, usuario: str, contrasena: str):
        usuario = usuario.strip()
        contrasena = contrasena.strip()

        for persona in self.usuarios:
            if (
                persona.usuario == usuario
                and persona.contrasena == contrasena
            ):
                return persona

        return None

    def listar_productos(self) -> list[Producto]:
        return self.productos.copy()

    def listar_usuarios(self) -> list[Usuario]:
        return self.usuarios.copy()

    def listar_ventas(self) -> list[Venta]:
        return self.ventas.copy()

    def cantidad_productos(self) -> int:
        return len(self.productos)

    def cantidad_usuarios(self) -> int:
        return len(self.usuarios)

    def buscar_producto(self, codigo: str):
        codigo = codigo.strip().upper()

        for producto in self.productos:
            if producto.codigo.upper() == codigo:
                return producto

        return None

    def buscar_usuario(self, usuario_id: str):
        usuario_id = usuario_id.strip()

        for usuario in self.usuarios:
            if usuario.usuario == usuario_id:
                return usuario

        return None

    def generar_identificador_venta(self) -> str:
        numero = len(self.ventas) + 1
        return f"V{numero:03d}"

    def registrar_venta(
        self,
        usuario_id: str,
        producto_codigo: str
    ) -> tuple[bool, str]:

        usuario_id = usuario_id.strip()
        producto_codigo = producto_codigo.strip().upper()

        if not usuario_id or not producto_codigo:
            return False, "Debe seleccionar un usuario y un producto."

        usuario = self.buscar_usuario(usuario_id)

        if not usuario:
            return False, "El usuario seleccionado no existe."

        producto = self.buscar_producto(producto_codigo)

        if not producto:
            return False, "El producto seleccionado no existe."

        nueva_venta = Venta(
            self.generar_identificador_venta(),
            usuario.usuario,
            producto.codigo,
            date.today().strftime("%d/%m/%Y")
        )

        self.ventas.append(nueva_venta)
        self._guardar_ventas()

        return True, "Venta registrada correctamente."

    def registrar_producto(
        self,
        codigo: str,
        nombre: str,
        categoria: str,
        precio: str,
        stock: str
    ) -> tuple[bool, str]:

        codigo = codigo.strip().upper()
        nombre = nombre.strip()
        categoria = categoria.strip()

        valido, mensaje, precio_numero, stock_numero = (
            self._validar_datos_producto(
                codigo,
                nombre,
                categoria,
                precio,
                stock
            )
        )

        if not valido:
            return False, mensaje

        if self.buscar_producto(codigo):
            return False, "Ya existe un producto con ese código."

        nuevo_producto = Producto(
            codigo,
            nombre,
            categoria,
            precio_numero,
            stock_numero
        )

        self.productos.append(nuevo_producto)
        self._guardar_productos()

        return True, "Producto registrado correctamente."

    def actualizar_producto(
        self,
        codigo: str,
        nombre: str,
        categoria: str,
        precio: str,
        stock: str
    ) -> tuple[bool, str]:

        codigo = codigo.strip().upper()
        nombre = nombre.strip()
        categoria = categoria.strip()

        producto = self.buscar_producto(codigo)

        if not producto:
            return False, "No existe un producto con ese código."

        valido, mensaje, precio_numero, stock_numero = (
            self._validar_datos_producto(
                codigo,
                nombre,
                categoria,
                precio,
                stock
            )
        )

        if not valido:
            return False, mensaje

        producto.nombre = nombre
        producto.categoria = categoria
        producto.precio = precio_numero
        producto.stock = stock_numero

        self._guardar_productos()

        return True, "Producto actualizado correctamente."

    def eliminar_producto(self, codigo: str) -> tuple[bool, str]:
        producto = self.buscar_producto(codigo)

        if not producto:
            return False, "No existe un producto con ese código."

        self.productos.remove(producto)
        self._guardar_productos()

        return True, "Producto eliminado correctamente."