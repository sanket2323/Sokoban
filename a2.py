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
        super().__init__()

    def __repr__(self) -> str:
        return "Wall()"

    def __str__(self) -> str:
        return WALL

    def get_type(self) -> str:
        return WALL

    def is_blocking(self) -> bool:
        return True


# task 4
class Goal(Tile):
    def __init__(self):
        self.is_filled_or_not = False

    def __str__(self) -> str:
        if not self.is_filled_or_not:
            return GOAL
        else:
            return FILLED_GOAL

    def __repr__(self) -> str:
        return "Goal()"

    def is_filled(self) -> bool:
        return self.is_filled_or_not

    def fill(self):
        self.is_filled_or_not = True

    def unfill(self):
        self.is_filled_or_not = False

    def get_type(self) -> str:
        return GOAL


# task 5
class Entity:
    def __init__(self, position: Position):
        self.position = position

    def __str__(self) -> str:
        return ENTITY

    def __repr__(self) -> str:
        x = self.position[0]
        y = self.position[1]
        return f"Entity(({x}, {y}))"

    def get_type(self) -> str:
        return ENTITY

    def get_position(self) -> Position:
        return self.position

    def set_position(self, new_pos: Position):
        self.position = new_pos


# task 6
class Potion(Entity):
    def __init__(self, position):
        super().__init__(position)

    def __str__(self) -> str:
        return POTION

    def __repr__(self) -> str:
        x = self.position[0]
        y = self.position[1]
        return f"Potion(({x}, {y}))"

    def get_type(self) -> str:
        return POTION

    def effect(self):
        return {}


# task 7
class StrengthPotion(Potion):
    def __init__(self, position):
        super().__init__(position)

    def __str__(self) -> str:
        return STRENGTH_POTION

    def __repr__(self) -> str:
        x = self.position[0]
        y = self.position[1]
        return f"StrengthPotion(({x}, {y}))"

    def get_type(self) -> str:
        return STRENGTH_POTION

    def effect(self):
        return {
            'strength': 2
        }


# task 8
class MovePotion(Potion):
    def __init__(self, position):
        super().__init__(position)

    def __str__(self) -> str:
        return MOVE_POTION

    def __repr__(self) -> str:
        x = self.position[0]
        y = self.position[1]
        return f"MovePotion(({x}, {y}))"

    def get_type(self) -> str:
        return MOVE_POTION

    def effect(self):
        return {
            'moves': 5
        }


def main() -> None:
    pass


if __name__ == "__main__":
    main()
