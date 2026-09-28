import tkinter as tk
from tkinter import ttk


class LoginView(tk.Frame):
    def __init__(
        self,
        master,
        restaurante_servicio,
        al_iniciar_sesion
    ) -> None:
        super().__init__(master)

        self.restaurante_servicio = restaurante_servicio
        self.al_iniciar_sesion = al_iniciar_sesion

        self.pack(fill="both", expand=True)

        self._crear_interfaz()

    def _crear_interfaz(self) -> None:
        contenedor = tk.Frame(self)
        contenedor.pack(expand=True)

        titulo = tk.Label(
            contenedor,
            text="Restaurante App",
            font=("Arial", 20, "bold")
        )
        titulo.pack(pady=10)

        subtitulo = tk.Label(
            contenedor,
            text="Inicio de sesión"
        )
        subtitulo.pack(pady=5)

        tk.Label(
            contenedor,
            text="Usuario:"
        ).pack(anchor="w")

        self.usuario_entry = tk.Entry(
            contenedor,
            width=30
        )
        self.usuario_entry.pack(pady=5)

        tk.Label(
            contenedor,
            text="Contraseña:"
        ).pack(anchor="w")

        self.contrasena_entry = tk.Entry(
            contenedor,
            width=30,
            show="*"
        )
        self.contrasena_entry.pack(pady=5)

        boton_ingresar = ttk.Button(
            contenedor,
            text="Iniciar sesión",
            command=self.iniciar_sesion
        )
        boton_ingresar.pack(pady=10)

        self.mensaje = tk.Label(
            contenedor,
            text=""
        )
        self.mensaje.pack(pady=5)

    def iniciar_sesion(self) -> None:
        usuario = self.usuario_entry.get().strip()
        contrasena = self.contrasena_entry.get().strip()

        if not usuario or not contrasena:
            self.mensaje.config(
                text="Ingrese usuario y contraseña."
            )
            return

        usuario_validado = (
            self.restaurante_servicio.validar_acceso(
                usuario,
                contrasena
            )
        )

        if usuario_validado is None:
            self.mensaje.config(
                text="Usuario o contraseña incorrectos."
            )
            return

        self.mensaje.config(text="")

        self.al_iniciar_sesion(
            usuario_validado
        )