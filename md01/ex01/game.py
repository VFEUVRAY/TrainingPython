From gotcharacter import GotCharacter

class Stark(GotCharacter):
    """Those guys live in the north something something
    I really don't want to write a whole book about them
    Because to be completely honest I stopped caring past season 4 xoxo
    """
    def __init__(self, first_name = None, is_alive = True):
        super().__init__(first_name, is_alive)
        self.family_name = "Stark"
        self.house_words = "Winter is Coming"

    def __dict__(self):
        print('')

    def print_house_words(self):
        print(self.house_words)
    
    def die(self):
        self.is_alive = False

