__author__ = 'Walter'
import os, plistlib
from urllib import parse

from pprint import pprint
from inspect import getmembers

class Itunes:

    def __init__(self, library):
        if not library:
            raise ItunesLibraryException('The library is missing or invalid')

        self.library = library
        self.tracks_sorted = self.get_tracks_keys_sorted()

    """ Returns <string> """
    def parse_music_location(self, music_location):
        return parse.unquote(music_location.replace('file://localhost/', ''))

    """ Returns <list> """
    def get_tracks_keys_sorted(self):
        return sorted(self.library['Tracks'].keys())

    """ Return <integer> rating total """
    def count_ratings(self, music_rating = 20):
        rating_count = 0

        for key in self.tracks_sorted:
            track = self.library['Tracks'][key]
            if(track.get('Rating') == music_rating):
                rating_count += 1

        return rating_count

    """ Delete all files filtering by rate """
    def delete_by_rating(self, music_rating = 20):
        rating_count = 0

        for key in self.tracks_sorted:
            track = self.library['Tracks'][key]
            music_location = self.parse_music_location(track.get('Location'))

            if(track.get('Rating') == music_rating):
                rating_count += 1
                try:
                    self.delete_file(music_location)
                except FileNotFoundError as e:
                    print(e)


        return rating_count

    """ """
    def delete_file(self, file_location):
        if(not os.path.isfile(file_location)):
            raise FileNotFoundError('Could not find de given file ', file_location)

        os.remove(file_location)

class ItunesLibraryException(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)