#!/usr/bin/python

from ConfigParser import SafeConfigParser


def main():
    parser = SafeConfigParser()
    parser.read('config.ini')

    print parser.get('person', 'name')

if __name__ == "__main__":
    main()
