from postac import Postac
import random

class Paladyn(Postac):

    def atak(self):
        return self.sila + random.randint(1, 6)