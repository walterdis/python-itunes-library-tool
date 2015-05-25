__author__ = 'Walter'
import os

""" Return the full file path if file exists """
def get_file(path, file_name = ''):
    if(os.path.isfile(path + file_name)):
        return path + file_name
    else:
        return False

