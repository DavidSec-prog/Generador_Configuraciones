"""
Módulo: utilidades/constantes.py
-------------------------------------------------------------------------------
Propósito:
    Almacenar todas las listas y diccionarios que definen las marcas de equipos,
    modelos y servicios disponibles en el generador de configuraciones.

Uso en la GUI:
    - VentanaPrincipal poblará los QComboBox con las claves y listas de este módulo.
    - El controlador usará las claves para construir la selección y buscar la plantilla.


    Para agregar un nuevo modelo de equipo o un nuevo tipo de
    servicio DEBE actualizar únicamente este archivo, sin tocar la lógica de negocio.

-------------------------------------------------------------------------------
"""

#Se crea un diccioanrio MARCAS_Y_MODELOS que relaciona cada marca con una lista de modelos disponibles

MARCAS_Y_MODELOS = {
    "Cisco": [
        "867",
        "C1111",
        "C921",
        "ISR 4321",
        "ISR 4431",
        "Catalyst 8000"
    ],
    "Huawei": [
        "AR161",
        "AR611",
        "AR617",
        "AR1220",
        "AR2220",
        "AR651"
    ],
    "Mikrotik": [
        "RB750"
    ],
    "Demarcador": [
        "RAX711",
        "TenGiga"
    ]
}

#Se crea un diccionario SERVICOS donde se relaciona todos los servicios a utilizar

SERVICIOS = [
    "Internet",
    "Telefonia (FTTx)",
    "MPLS (con BGP)",
    "Telefonia SIP (FTTO)"
]