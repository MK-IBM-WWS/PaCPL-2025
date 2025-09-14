from abc import ABC, abstractmethod

class GeometricalShape(ABC):
    @abstractmethod
    def area(self)->float:
        pass

    @abstractmethod
    def get_name(self)->str:
        pass

    @abstractmethod
    def draw(self, ax)->None:
        pass

    @abstractmethod
    def __repr__(self):
        pass