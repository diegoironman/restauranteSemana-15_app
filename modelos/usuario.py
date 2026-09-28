class Usuario:
    def __init__(self, usuario: str, nombre: str, contrasena: str) -> None:
        self.usuario = usuario
        self.nombre = nombre
        self.contrasena = contrasena

    def __str__(self) -> str:
        return f"{self.usuario} - {self.nombre}"