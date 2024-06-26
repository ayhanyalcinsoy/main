#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get


def setup():
    shelltools.makedirs("build")
    shelltools.cd("build")

    cmaketools.configure("-DCMAKE_INSTALL_PREFIX=/usr \
      -DBUILD_PLUGIN_PGPOINTCLOUD=ON \
      -DBUILD_PGPOINTCLOUD_TESTS:BOOL=OFF \
      -DWITH_COMPLETION=ON", sourceDir="..")

def build():
    shelltools.cd("build")
    cmaketools.make()

def check():
    pass
    #cmaketools.make("test")


def install():
    shelltools.cd("build")
    cmaketools.install()

    shelltools.cd("..")
    pisitools.dodoc("README.md", "LICENSE*")
