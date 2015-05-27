
__author__ = 'Walter Discher Cechinel'

import getpass, util.base
import plistlib

class Reader:
    def __init__(self):
        self.location = ''
        self.file_name = 'iTunes Music Library.xml'

    def load(self, full_file_path=''):
        file = self.__get_file(full_file_path) if full_file_path else self.__get_file()
        self.location = full_file_path if file is False else file

        if not file:
            return False

        with open(file, 'rb') as library:
            return plistlib.load(library)

    def __get_file(self, full_file_path = ''):
        if full_file_path:
            return util.base.get_file(full_file_path)

        for path in Reader.__get_file_paths():
            full_file_path = util.base.get_file(path, self.file_name)

            if full_file_path:
                return full_file_path

        return False

    @staticmethod
    def __get_file_paths():
        return [
            r'C:\Documents and Settings\{!s}\My Documents\My Music\iTunes\\'.format( getpass.getuser() ),
            r'C:\Users\{!s}\Music\iTunes\\'.format( getpass.getuser() ),
            r'C:\Users\{!s}\My Music\iTunes\\'.format( getpass.getuser() ),
            r'C:\Users\{!s}\My Music\iTunes\\'.format( getpass.getuser() ),
        ]