#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Walter Discher Cechinel'

import os
import platform
from itunes.reader import Reader
from itunes.itunes import Itunes, ItunesLibraryException
from menu import Menu
from command import Command

if hasattr(platform, 'linux_distribution'):
    os.system('clear')
else:
    os.system('cls')

reader = Reader()
library = reader.load()


while(not library):
    print(r"""
    Can't find the file %s
    ------------------------------------------------------------
    Please provide the Itunes library file location with full path
        - Example: C:\Users\your_username\My Music\iTunes\iTunes Music Library.xml

    """ % reader.location)

    library_location = input('File location: ')
    library = reader.load(library_location)
try:
    itunes = Itunes(library)
    menu = Menu(reader.location, Command(itunes), itunes)

    os.system('clear')
    menu.main()
except ItunesLibraryException as e:
    print(e)



