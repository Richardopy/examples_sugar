# -*- coding: utf-8 -*-
# Copyright 2009 Simon Schampijer
# Copyright 2013 Martin Abente
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA

"""HelloWorld Activity: A case study for developing an activity."""

import gtk
import logging
from datetime import datetime

from gettext import gettext as _

from sugar.activity import activity
from sugar.graphics.toolbarbox import ToolbarBox
from sugar.activity.widgets import ActivityButton
from sugar.activity.widgets import ActivityToolbox
from sugar.activity.widgets import TitleEntry
from sugar.activity.widgets import StopButton
from sugar.activity.widgets import ShareButton

class HelloWorldActivity(activity.Activity):
    """HelloWorldActivity class as specified in activity.info"""

    def __init__(self, handle):
        """Set up the HelloWorld activity."""
        activity.Activity.__init__(self, handle)

        # we do not have collaboration features
        # make the share option insensitive
        self.max_participants = 1

        # toolbar with the new toolbar redesign
        toolbar_box = ToolbarBox()

        activity_button = ActivityButton(self)
        toolbar_box.toolbar.insert(activity_button, 0)
        activity_button.show()

        title_entry = TitleEntry(self)
        toolbar_box.toolbar.insert(title_entry, -1)
        title_entry.show()

        share_button = ShareButton(self)
        toolbar_box.toolbar.insert(share_button, -1)
        share_button.show()
        
        separator = gtk.SeparatorToolItem()
        separator.props.draw = False
        separator.set_expand(True)
        toolbar_box.toolbar.insert(separator, -1)
        separator.show()

        stop_button = StopButton(self)
        toolbar_box.toolbar.insert(stop_button, -1)
        stop_button.show()

        self.set_toolbar_box(toolbar_box)
        toolbar_box.show()

        # advanced example widgets
        vbox = gtk.VBox()
        self.label = gtk.Label()
        self.entry = gtk.Entry()
        self.text = gtk.TextView()

        vbox.add(self.label)
        vbox.add(self.entry)
        vbox.add(self.text)

        self.set_canvas(vbox)
        vbox.show_all()

        self._logging_example()
        self._i18n_example()

    def _logging_example(self):
        """ Suppose we want to log specific info"""

        # It will initialized with sugar global level
        # logging.setLevel(logging.DEBUG)

        # debug is typically the proper replacement for random prints
        logging.debug("I want to log the fact that I got here, but not always")

        # info is the proper way to log messages during normal executions 
        logging.info("Got to this point at %s ...", datetime.now())

        # error is used when there something wrong happening, but is expected
        logging.error("Maybe some value was out of its expected range")

        # exception is the proper way to log our exceptions
        try:
            somefile = file("wont-find-this-file")
        except IOError:
            logging.exception("The file was not found")

    def _i18n_example(self):
        """ How-to work with i18n"""
    
        # the i18n strings are stored at po/ directory
        # to generate the i18n table: ./setup.py genpot
        i18n_string = _("Hello World!")
        self.label.set_text(i18n_string)

    def read_file(self, tmp_file):
        """ datastore high-level interaction to read """
        logging.debug("The tmp_file is at %s, for reading", tmp_file)

        # resume metadata
        try:
            self.entry.set_text(self.metadata['entry'])
        except KeyError:
            logging.error("No entry metadata")

        # resume data
        data = open(tmp_file, "r")
        buffer = self.text.get_buffer()
        buffer.set_text(data.read())
        data.close()

    def write_file(self, tmp_file):
        """ datastore high-level interaction to write """
        logging.debug("The tmp_file is at %s, for writing", tmp_file)

        # save metadata
        self.metadata['entry'] = self.entry.get_text()

        # save data
        data = open(tmp_file, "w")
        buffer = self.text.get_buffer()
        data.write(buffer.get_text(*buffer.get_bounds()))
        data.close()
