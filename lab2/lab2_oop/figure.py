from abc import ABC, abstractmethod


class Figure(ABC):
    @abstractmethod
    def mesure(self):
        pass
