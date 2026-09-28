# Restaurante App - Semana 14

## Propósito

Este proyecto corresponde a la Semana 14 de Programación Orientada a Objetos. Su objetivo es aplicar componentes y contenedores de Tkinter para mejorar la interfaz gráfica de un sistema de restaurante, manteniendo una arquitectura modular y la persistencia de datos en archivos JSON.

## Estructura del proyecto

```text
restaurante_app/
├── datos/
│   ├── productos.json
│   └── usuarios.json
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   └── usuario.py
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante_servicio.py
├── ui/
│   ├── __init__.py
│   ├── login_view.py
│   └── main_view.py
├── main.py
└── README.md