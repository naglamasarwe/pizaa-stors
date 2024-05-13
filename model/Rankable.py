from abc import ABC, abstractmethod


@abstractmethod
class Rankble(ABC):
    def calculate_rank(self):
        pass
