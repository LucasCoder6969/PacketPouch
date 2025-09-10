import socket
from typing import Union

class SockSock(socket.socket):
    """Wrapper around socket.socket with default TCP settings."""
    def __init__(self):
        super().__init__(socket.AF_INET, socket.SOCK_STREAM)


def socketConnect(sock: SockSock, address: tuple[str, int]) -> None:
    """
    Connect a socket to a given address.

    Parameters:
        sock: SockSock instance
        address: tuple (host, port), e.g., ('127.0.0.1', 8080)
    """
    sock.connect(address)

def socketClose(sock: SockSock) -> None:
    """
    Close an socket.
    Parameters:
        sock: SockSock instance
    """
    sock.close()

def socketSend(sock: SockSock, data: Union[bytes, bytearray, memoryview]) -> int:
    """
    Send data through a socket.

    Parameters:
        sock: SockSock instance
        data: bytes-like object to send

    Returns:
        Number of bytes sent.
    """
    return sock.send(data)

def socketSendAll(sock: SockSock, data: Union[bytes, bytearray, memoryview]):
    """
    Send all data through a socket (blocking until complete).
    """
    sock.sendall(data)
