"""
Propósito:
    Proporcionar funciones para validar direcciones IP, prefijos de máscara
    y números de VLAN según las reglas del generador de configuraciones.

Uso:
    Se importan desde la interfaz gráfica (para mostrar errores en tiempo real)
    y desde las plantillas (para asegurar datos correctos antes de generar).
"""


import ipaddress
from typing import Union

def validar_ip(ip_str: str) -> bool:

    """
    Verifica si una cadena es una dirección IPv4 válida (formato decimal
    con cuatro octetos entre 0 y 255, sin segmentos vacíos).

    Parámetros:
        ip_str: texto con la IP a evaluar.

    Retorna:
        True si es válida, False si no.
    """
    try:
        # Crea un objeto IPv4Address. Si la cadena no cumple el formato
        # o los octetos están fuera de rango, lanza AddressValueError.
        ipaddress.IPv4Address(ip_str)
        return True #IP valida
    except ipaddress.AddressValueError:
        return False    #Error formato o rango
    except Exception:  # Captura cualquier otro error inesperado
        return False
    


def validar_prefijo(mascara: str) -> bool:
    """
    Verifica si una máscara de subred (en notación de longitud de prefijo
    o en formato decimal) es válida para la WAN. Solo se permiten los
    prefijos 21-24 y 30.

    Parámetros:
        mascara: texto ingresado por el usuario (ej: '24' o '255.255.255.0').

    Retorna:
        True si es un prefijo válido, False en caso contrario.
    """
    try:
        # convertir a entero (notación de prefijo).
        prefijo = int(mascara)
        return prefijo == 30 or (21 <= prefijo <= 24)   # Retorna True solo si el entero es 30 o está entre 21 y 24.

    except ValueError:
        # interpretar como máscara decimal 
        try:
            red = ipaddress.IPv4Network(f"0.0.0.0/{mascara}", strict=False) #se crea una Ip 0.0.0.0 /mascara -- strict=flase exoija que la amscara no sea 0.0.0.0
            return red.prefixlen == 30 or (21 <= red.prefixlen <= 24) 
        except (ipaddress.NetmaskValueError, ValueError, TypeError):
            return False             # Si la máscara no es válida, se captura la excepción y se retorna False.

        

def validar_vlan(vlan_str: str) -> bool:
    """
    Comprueba que un número de VLAN esté en el rango permitido (2 a 4094).

    Parámetros:
        vlan_str: texto con el número de VLAN.

    Retorna:
        True si es un entero entre 2 y 4094, False en cualquier otro caso.
    """
    try:
        vlan = int(vlan_str)
        return 2 <= vlan <= 4094 # Verifica el rango 
    except (ValueError, TypeError):
        return False
    