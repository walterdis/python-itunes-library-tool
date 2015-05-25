#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Walter Discher Cechinel'

import util.base, os, getpass
from itunes import Itunes
from menu import Menu
from command import Command

os.system('cls')

file_path = r'C:\Users\{!s}\Music\iTunes/'.format( getpass.getuser() )
file_name = 'iTunes Music Library.xl'

location = file_name+file_name
xml_file = util.base.get_file(file_path, file_name)

while(not xml_file):
    print(r"""
    Can't find the file %s
    ------------------------------------------------------------
    Please provide de Itunes library file location with full path
        - Example: C:\Users\your_username\My Music\iTunes\iTunes Music Library.xml

    """ % location)

    location = input('File location: ')
    xml_file = util.base.get_file(location)

itunes = Itunes(xml_file)
menu = Menu(xml_file, Command(itunes), itunes)

menu.main()