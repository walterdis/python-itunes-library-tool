__author__ = 'Walter'

class Command:

    def __init__(self, object):
        self.object = object

    """ """
    def execute(self, command, options = None):

        commands = {
            1: self.count_ratings,
            2: self.delete_by_rating
        }

        commands[command]()

    """ """
    def count_ratings(self):
        ratings = [20, 40, 60, 80, 100]
        value = int(input('Give a value between 1 and 5: '))

        count = self.object.count_ratings(ratings[value -1])

        output = 'Found {!s} files with the given rate: {!s}'.format(count, value)
        self.output(output)

    """ """
    def delete_by_rating(self):
        self.output('Not implemented yet')

    """ """
    def output(self, output):
        print(output)