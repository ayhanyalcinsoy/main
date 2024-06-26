#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools

def setup():
    shelltools.cd("libraries/source/spidermonkey")
    shelltools.system("mkdir -p mozjs-78.6.0/.git")
    shelltools.cd("../../..")

    shelltools.cd("build/workspaces/")
    shelltools.chmod("update-workspaces.sh", 0755)
    shelltools.export("WX_CONFIG", "/usr/bin/wxconfig")
    shelltools.export("SHELL","SHELL=/bin/bash")
    
    shelltools.system("sh update-workspaces.sh \
                       --bindir=/usr/bin \
                       --disable-atlas \
                       --without-pch \
                       --libdir=/usr/lib/0ad \
                       --datadir=/usr/share/0ad/data \
                       JOBS=%s" % get.makeJOBS())

def build():
    shelltools.cd("build/workspaces/gcc")
    autotools.make()

def install():
    pisitools.dodoc("LICENSE.txt","license_dbghelp.txt","license_gpl-2.0.txt","license_lgpl-2.1.txt","README.txt",)
    pisitools.insinto("/usr/share/0ad", "binaries/*")
    pisitools.insinto("/usr/bin/", "binaries/system/pyrogenesis")
    pisitools.insinto("/usr/lib/0ad/", "binaries/system/*.so*")
    pisitools.insinto("/usr/bin/", "build/resources/0ad.sh")
    pisitools.insinto("/usr/share/pixmaps/", "build/resources/0ad.png", "0ad.png")
    pisitools.insinto("/usr/share/applications/", "build/resources/0ad.desktop", "0ad.desktop")
