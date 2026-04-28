import sys
import os
from unittest.mock import patch, MagicMock
import socket

# Add src to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from scan import PortScanner

def test_port_scanner_init():
    scanner = PortScanner("127.0.0.1")
    assert scanner.host == "127.0.0.1"
    assert scanner.tcp_ports == []
    assert scanner.udp_ports == []

@patch('socket.socket')
def test_scan_tcp_open(mock_socket):
    # Setup mock
    mock_s = MagicMock()
    mock_s.connect_ex.return_value = 0 # Success
    mock_socket.return_value.__enter__.return_value = mock_s
    
    scanner = PortScanner("1.2.3.4")
    result = scanner.scan_tcp(80)
    
    assert result is True
    assert 80 in scanner.tcp_ports
    mock_s.connect_ex.assert_called_with(("1.2.3.4", 80))

@patch('socket.socket')
def test_scan_tcp_closed(mock_socket):
    # Setup mock
    mock_s = MagicMock()
    mock_s.connect_ex.return_value = 111 # Connection refused
    mock_socket.return_value.__enter__.return_value = mock_s
    
    scanner = PortScanner("1.2.3.4")
    result = scanner.scan_tcp(80)
    
    assert result is False
    assert 80 not in scanner.tcp_ports

@patch('socket.socket')
def test_scan_udp_open(mock_socket):
    # Setup mock
    mock_s = MagicMock()
    mock_s.recvfrom.return_value = (b"data", ("1.2.3.4", 53))
    mock_socket.return_value.__enter__.return_value = mock_s
    
    scanner = PortScanner("1.2.3.4")
    result = scanner.scan_udp(53)
    
    assert result is True
    assert 53 in scanner.udp_ports
    mock_s.sendto.assert_called()

@patch('socket.socket')
def test_scan_udp_timeout(mock_socket):
    # Setup mock
    mock_s = MagicMock()
    mock_s.recvfrom.side_effect = socket.timeout
    mock_socket.return_value.__enter__.return_value = mock_s
    
    scanner = PortScanner("1.2.3.4")
    result = scanner.scan_udp(53)
    
    assert result is False
    assert 53 not in scanner.udp_ports
