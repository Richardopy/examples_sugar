#!/usr/bin/python


class MyClass(object):

    def __init__(self, name, lastname=''):
        self.name = name
        self.lastname = lastname

    def get_fullname(self):
        fullname = '%s %s' % (self.name, self.lastname)
        fullname.strip()
        return fullname


def main():
    myclass = MyClass('Google', 'code in')
    print myclass.get_fullname()

if __name__ == "__main__":
    main()
