from abc import ABC, abstractmethod

class Postac(ABC):    # KLASA ABSTRAKCYJNA
    def __init__(self, sila, wiedza):
        self.sila = sila
        self.wiedza = wiedza

    @abstractmethod
    def atak(self):
        pass