#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools, get

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
	

