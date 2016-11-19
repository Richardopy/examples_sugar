#!/usr/bin/python

import gobject


def print_something():
    print 'Hello world!'
    return True


def main():
    gobject.timeout_add(1000, print_something)
    gobject.MainLoop().run()

if __name__ == "__main__":
    main()
