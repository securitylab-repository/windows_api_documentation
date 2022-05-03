#######################################################################
# Copyright (c) 2020
# Boussad AIT SALEM <boussad.aitsalem<at>gmail<dot>com>
# All rights reserved.
########################################################################
#
#  This file is part of msdn plugin of IDA PRO
#
#  MSDN_IDAPRO is free software: you can redistribute it and/or modify it
#  under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful, but
#  WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#  General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see
#  <http://www.gnu.org/licenses/>.
#
########################################################################

from idaapi import *
from idautils import * 
from subprocess import Popen
import webbrowser

import ida_kernwin



def hotkey_pressed():
    search = None

    for xref in XrefsFrom(here(), 0):

        if xref.type == fl_CN or xref.type == fl_CF:
            search = get_name(xref.to)

    if search:

        feed_url = "https://docs.microsoft.com/en-US/search/?terms={}".format(search)

        webbrowser.open(feed_url)
    else:
        print("FAILED: Nothing found to search.")



try:
    hotkey_ctx
    if ida_kernwin.del_hotkey(hotkey_ctx):
        print("Hotkey unregistered!")
        del hotkey_ctx
    else:
        print("Failed to delete hotkey!")
except:
    hotkey_ctx = ida_kernwin.add_hotkey("Shift-H", hotkey_pressed)
    if hotkey_ctx is None:
        print("Failed to register hotkey!")
        del hotkey_ctx
    else:
        print("Hotkey registered!")


