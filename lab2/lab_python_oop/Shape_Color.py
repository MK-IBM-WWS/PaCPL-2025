from enum import Enum

class Color(Enum):
    BLUE = "blue"
    RED = "red"
    GREEN = "green"

    def __str__(self):
        return self.value



