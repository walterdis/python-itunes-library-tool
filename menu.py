__author__ = 'Walter'

class Menu:

    def __init__(self, library_location, commander, object):
        self.library_location = library_location
        self.commander = commander
        self.object = object


    def main(self):
        print(
        """
        ITunes library location: %s
            - Press 1 to count files by rating
            - Press 2 to delete files by rating
        """ %
        self.library_location
        )

        command = int(input('Select an option above: '))
        self.commander.execute(command)


