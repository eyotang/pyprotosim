#-----------------------------------------------------------------------------
#   Copyright (c) 2015-2022, Ben Tang All rights reserved.
#
#   Released under the BSD license. See the LICENSE file for details.
#-----------------------------------------------------------------------------
"""A Python library for loading diameter over tcp or sctp."""

#: Version info (major, minor, maintenance, status)
VERSION = (0, 7, 15)
STATUS = ''
__version__ = '%d.%d.%d' % VERSION[0:3] + STATUS

import sys as _sys

if _sys.version_info[0:2] < (2, 4):
    raise RuntimeError('Python 2.4.x or higher is required!')

from ctypes import cdll
lib1 = cdll.LoadLibrary('./libDiameter/sctp/libsctp.so')

from libDiameter.Socket import (TcpSocket, SctpSocket)
from libDiameter.libDiameterImp import *
