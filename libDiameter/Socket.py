import sys

import sctp
import _sctp
import socket

from sctp import *

from abc import ABCMeta, abstractmethod


class IConnectionSocket(object):
    '''
    Abstract connection socket
    '''

    __metaclass__ = ABCMeta

    @abstractmethod
    def __init__(self):
        self._sock = None
        pass

    def socket(self):
        return self._sock

    def setsockopt(self, level, optname, value):
        self._sock.setsockopt(level, optname, value)
        pass

    def bind(self, saddr):
        self._sock.bind(saddr)
        pass

    def listen(self, backlog):
        self._sock.listen(backlog)
        pass

    def accept(self):
        return self._sock.accept()

    def connect(self, saddr):
        self._sock.connect(saddr)
        pass

    def send(self, buf):
        self._sock.send(buf)
        pass

    def recv(self, bufsize):
        return self._sock.recv(bufsize)

    def close(self):
        self._sock.close()
        pass

    def getpeername(self):
        return self._sock.getpeername()

    def getsockname(self):
        return self._sock.getsockname()

class TcpSocket(IConnectionSocket):
    '''
    TCP socket
    '''
    def __init__(self):
        super(TcpSocket, self).__init__()
        self._sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        pass

class SctpSocket(IConnectionSocket):
    '''
    SCTP socket
    '''
    def __init__(self):
        super(SctpSocket, self).__init__()
        self._sock = sctpsocket_tcp(socket.AF_INET)
        pass

    def send(self, buf):
        self._sock.sctp_send(buf)
        pass

    def recv(self, buf_size):
        (_fromaddr, _flags, msg, _notif) =  self._sock.sctp_recv(buf_size)
        return msg
