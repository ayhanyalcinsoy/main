#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import scons

def build():
    scons.make("PREFIX=/usr/ LIBDIR=/usr/lib GSSAPI=/usr/bin/krb5-config")

def install():
    pisitools.insinto("/usr/include/serf-1/", "serf*.h")
    pisitools.insinto("/usr/lib/", "libserf-1*")
    pisitools.insinto("/usr/lib/pkgconfig/", "serf-1.pc")
    
    pisitools.dodoc("CHANGES", "LICENSE", "NOTICE", "README")
