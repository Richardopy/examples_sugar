#!/usr/bin/python
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GObject


OPTIONS = ['a', 'b', 'c', 'd']
OPT_LENGHT = 4
DELAY = 1000

class Teclado(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Vocal")
        self.set_border_width(10)

        vbox = Gtk.VBox()
        hbox = Gtk.HBox()
        label = Gtk.Label()

        self.add(vbox)
        vbox.add(label)
        vbox.add(hbox)

        for option in OPTIONS:
            button = Gtk.Button()
            button.set_label(option)
            button.connect('activate', self.__button_cb, label, option)

            hbox.add(button)

        self._button_index = 0
        GObject.timeout_add(DELAY, self.__timeout_cb, hbox)

    def __button_cb(self, button, label, option):
        label.set_text(option)

    def __timeout_cb(self, hbox):
        self._button_index = (self._button_index + 1) % OPT_LENGHT

        buttons = hbox.get_children()
        button = buttons[self._button_index]
        button.grab_focus()

        return True

win = Teclado()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
