#!/usr/bin/python
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk

class Teclado(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Grabbing keys example.")
        self.set_border_width(10)

        label = Gtk.Label("Press any key.")
        self.add(label)
        self.connect('key-press-event', self.__key_press_cb, label)

    def __key_press_cb(self, window, event, label):
        key_name = Gdk.keyval_name(event.keyval)
        label.set_text(key_name)

win = Teclado()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()