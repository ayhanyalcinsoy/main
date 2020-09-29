#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2013 Alokin Software Pvt Ltd.
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    autotools.configure()

    # fix unused direct dependency analysis
    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")


def build():
    autotools.make("-j1")


def install():
    autotools.rawInstall('DESTDIR=%s' % get.installDIR())

    pisitools.dodoc("README*", "LICENSE*", "COPYING", "SECURITY*")
