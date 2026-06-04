"""
Módulo: modelos/calculadora_ip.py
-------------------------------------------------------------------------------
Propósito:
    Realizar todos los cálculos de subred (red, broadcast, máscara, wildcard,
    primer/último host).

-------------------------------------------------------------------------------
"""
import ipaddress
from typing import List, Optional

# Función auxiliar interna para crear un objeto IPv4Network
def _validar_ip_prefijo(ip: str, prefijo: int) -> ipaddress.IPv4Network:
    """
    Crea un objeto IPv4Network a partir de una IP y un prefijo.
    strict=False permite que la IP no sea necesariamente la dirección de red.
    """
    return ipaddress.IPv4Network(f"{ip}/{prefijo}", strict=False)



def ip_to_vector(ip: str) -> List[int]:
    """
    Convierte una IP en una lista de sus cuatro octetos.

    Parámetros:
        ip: cadena con la IP (ej: '192.168.1.1').

    Retorna:
        Lista de 4 enteros.
    """
    # Divide la cadena por '.' y convierte cada parte en entero
    return [int(octeto) for octeto in ip.split('.')]



def vector_to_ip(vector: List[int]) -> str:
    """
    Convierte una lista de cuatro octetos en una cadena IP.

    Parámetros:
        vector: lista de 4 enteros.

    Retorna:
        IP en formato decimal.
    """
    # Une los octetos con puntos
    return f"{vector[0]}.{vector[1]}.{vector[2]}.{vector[3]}"



def prefix_to_mask(prefijo: int) -> str:
    """
    Obtiene la máscara de subred en notación decimal a partir de la
    longitud de prefijo.

    Parámetros:
        prefijo: entero entre 0 y 32.

    Retorna:
        Máscara decimal (ej: '255.255.255.0' para prefijo 24).
    """
    # Se crea una red  con IP 0.0.0.0 y el prefijo indicado
    red = ipaddress.IPv4Network(f"0.0.0.0/{prefijo}", strict=False)
    # Se extrae la máscara de red en formato decimal
    return str(red.netmask)



def mask_to_wildcard(mascara: str) -> str:
    """
    Convierte una máscara de red en su wildcard (máscara inversa).

    Parámetros:
        mascara: máscara en formato decimal (ej: '255.255.255.0').

    Retorna:
        Wildcard correspondiente (ej: '0.0.0.255').
    """
    # Se crea una red con la máscara dada para obtener el hostmask
    red = ipaddress.IPv4Network(f"0.0.0.0/{mascara}", strict=False)
    # El atributo hostmask es la wildcard (cada bit de host es 1)
    return str(red.hostmask)



def calcular_network(ip: str, prefijo: int) -> str:
    """
    Calcula la dirección de red a la que pertenece una IP.

    Parámetros:
        ip: IP de referencia.
        prefijo: longitud de prefijo.

    Retorna:
        Dirección de red (ej: '192.168.1.0').
    """
    red = _validar_ip_prefijo(ip, prefijo)
    return str(red.network_address)




def calcular_broadcast(ip: str, prefijo: int) -> str:
    red = _validar_ip_prefijo(ip, prefijo)
    return str(red.broadcast_address)




def obtener_host_min(ip: str, prefijo: int) -> str:
    red = _validar_ip_prefijo(ip, prefijo)
    return str(red.network_address + 1)




def obtener_host_max(ip: str, prefijo: int) -> str:
    red = _validar_ip_prefijo(ip, prefijo)
    return str(red.broadcast_address - 1)




def ip_para_configuracion_wan(ip: str, prefijo: int) -> str:
    if prefijo == 30:
        return obtener_host_max(ip, prefijo)
    return ip





def obtener_info_subred(ip: str, prefijo: int) -> dict:
    red = _validar_ip_prefijo(ip, prefijo)
    info = {
        'ip': ip,
        'prefijo': red.prefixlen,
        'mascara': str(red.netmask),
        'wildcard': str(red.hostmask),
        'red': str(red.network_address),
        'broadcast': str(red.broadcast_address),
        'host_min': obtener_host_min(ip, prefijo),
        'host_max': obtener_host_max(ip, prefijo),
        'ip_wan': ip_para_configuracion_wan(ip, prefijo)
    }
    return info