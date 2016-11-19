#!/usr/bin/python
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class ButtonWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Ventana")
        self.set_border_width(10)

        hbox = Gtk.HBox()
        self.add(hbox)

        title = Gtk.Label("Title")
        hbox.add(title)

        vbox = Gtk.VBox()
        hbox.add(vbox)

        button1 = Gtk.Button("Open")
        button2 = Gtk.Button("Save")
        button3 = Gtk.Button("Quit")
        vbox.add(button1)
        vbox.add(button2)
        vbox.add(button3)

win = ButtonWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
