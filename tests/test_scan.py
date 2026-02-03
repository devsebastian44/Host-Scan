import os
import sys

# Agregar la ruta src para que pytest encuentre el módulo
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

# Evitamos importar la ejecución del __main__ real para que no bloquee los tests esperando input
import scan

def test_imports():
    """Prueba básica para validar que el script se puede importar sin errores de sintaxis"""
    assert scan is not None

def test_tcp_ports_list_exists():
    """Valida la existencia de las listas para recolectar puertos"""
    assert isinstance(scan.tcp_ports, list)
    assert isinstance(scan.udp_ports, list)
