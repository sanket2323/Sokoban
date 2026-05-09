# DO NOT modify or add any import statements
from support import *


# Name:Sanket Mane
# Student Number: 50040467
# Favorite Box: 
# -----------------------------------------------------------------------------

# Define your classes and functions here

# task 1
class Tile:

    def __init__(self):
        pass

    def __str__(self) -> str:
        return TILE

    def __repr__(self) -> str:
        return "Tile()"

    def get_type(self) -> str:
        return TILE

    def is_blocking(self) -> bool:
        return False


# task 2
class Floor(Tile):
    def __init__(self):
        super().__init__()

    def __repr__(self) -> str:
        return "Floor()"

    def __str__(self) -> str:
        return FLOOR

    def get_type(self) -> str:
        return FLOOR


# task 3
class Wall(Tile):
    def __init__(self):
        pass

    def __repr__(self) -> str:
        return "Wall()"

    def __str__(self) -> str:
        return WALL

    def get_type(self) -> str:
        return WALL

    def is_blocking(self) -> bool:
        return True


def main() -> None:
    pass


if __name__ == "__main__":
    main()
