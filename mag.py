from postac import Postac
import random

class Mag(Postac):

    def atak(self):
        return self.wiedza + random.randint(1, 6)