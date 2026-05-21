# DO NOT modify or add any import statements
from sys import flags

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


# task 9
class FancyPotion(Potion):
    def __init__(self, position):
        super().__init__(position)

    def __str__(self) -> str:
        return FANCY_POTION

    def __repr__(self) -> str:
        x = self.position[0]
        y = self.position[1]
        return f"FancyPotion(({x}, {y}))"

    def get_type(self) -> str:
        return FANCY_POTION

    def effect(self):
        return {
            'strength': 2,
            'moves': 2
        }


# task 10
class Crate(Entity):

    def __init__(self, position, weight):
        super().__init__(position)
        self.weight = weight

    def __str__(self):
        return str(self.weight)

    def __repr__(self) -> str:
        x = self.position[0]
        y = self.position[1]
        z = self.weight
        return f"Crate(({x}, {y}), {z})"

    def get_weight(self):
        return self.weight

    def get_type(self) -> str:
        return CRATE


# task 11
class Player(Entity):

    def __init__(self, position: Position, strength: int, moves_remaining: int):
        super().__init__(position)
        self.strength = strength
        self.moves_remaining = moves_remaining

    def __str__(self):
        return PLAYER

    def __repr__(self) -> str:
        w = self.position[0]
        x = self.position[1]
        y = self.strength
        z = self.moves_remaining
        return f"Player(({w}, {x}), {y}, {z})"

    def get_type(self) -> str:
        return PLAYER

    def get_strength(self) -> int:
        return self.strength

    def add_strength(self, strength):
        self.strength += strength

    def get_moves_remaining(self) -> int:
        return self.moves_remaining

    def add_moves_remaining(self, moves):
        self.moves_remaining += moves

    def apply_effect(self, potion_effect):
        strength_value = 0
        moves_value = 0
        if 'strength' in potion_effect:
            strength_value = potion_effect['strength']

        if 'moves' in potion_effect:
            moves_value = potion_effect['moves']
        self.add_strength(strength_value)
        self.add_moves_remaining(moves_value)


# task 12
def read_file(maze_file: str) -> tuple[Maze, list[Entity], Player]:
    file = open(maze_file)
    lines = file.readlines()
    steps = lines[0].split(" ")

    strength = int(steps[0])
    moves = int(steps[1])
    maze = []
    entity = []
    player = []

    for row_index, line in enumerate(lines[1:]):

        inner_row = []
        for col_index, char in enumerate(line):
            # building Maze
            if char == 'W':
                inner_row.append(Wall())
            elif char == 'G':
                inner_row.append(Goal())
            elif char == '\n':
                pass
            else:
                inner_row.append(Floor())

            # building Entity
            position = (row_index, col_index)
            weight = char
            if char.isdigit():
                entity.append(Crate(position, int(weight)))

            elif char == 'P':
                player.append(Player(position, strength, moves))

            elif char == 'S':
                entity.append(StrengthPotion(position))

            elif char == 'F':
                entity.append(FancyPotion(position))

            elif char == 'M':
                entity.append(MovePotion(position))

        maze.append(inner_row)

    return maze, entity, player[0]


# task 13
class SokobanModel:
    def __init__(self, maze, entities, player):
        self.maze = maze
        self.entities = entities
        self.player = player

    def get_maze(self) -> Maze:
        return self.maze

    def get_entities(self) -> list[Entity]:
        return self.entities

    def get_player(self):
        return self.player

    def entity_positions(self) -> dict[Position, Entity]:
        position_dict = {}
        for entity in self.entities:
            position_dict[entity.get_position()] = entity
        return position_dict

    def has_won(self) -> bool:
        for row in self.maze:
            for tile in row:
                if tile.get_type() == GOAL and not tile.is_filled():
                    return False
        return True

    def has_lost(self) -> bool:
        if self.player.get_moves_remaining() <= 0 and not self.has_won():
            return True
        return False

    def shove_crate(self, crate, direction) -> bool:

        valid_direction_list = ['w', 'W', 'a', 'A', 's', 'S', 'd', 'D']

        # check if the direction is valid direction
        if direction not in valid_direction_list:
            return False

        # strength check
        if self.player.get_strength() < crate.get_weight():
            return False
        row, col = crate.get_position()

        # calculate new positions
        if direction.lower() == 'w':
            new_position = (row - 1, col)

        elif direction.lower() == 'a':
            new_position = (row, col - 1)

        elif direction.lower() == 's':
            new_position = (row + 1, col)

        else:
            new_position = (row, col + 1)

        # check if new_position is wall or another entity
        maze = self.get_maze()

        if maze[new_position[0]][new_position[1]].is_blocking():
            return False

        # check if another entity exist or not

        entiny_position = self.entity_positions()

        if new_position in entiny_position:
            return False

        # old position of crate
        old_row, old_col = crate.get_position()

        # unfill the goal
        if maze[old_row][old_col].get_type() == GOAL:
            self.maze[old_row][old_col].unfill()

        # move crate
        crate.set_position(new_position)

        new_row, new_col = new_position
        if self.maze[new_row][new_col].get_type() == GOAL:
            self.maze[new_row][new_col].fill()

        return True

    def attempt_move(self, direction: str) -> bool:
        valid_direction_list = ['w', 'W', 'a', 'A', 's', 'S', 'd', 'D']

        # invalid direction
        if direction not in valid_direction_list:
            return False

        # current player position
        row, col = self.player.get_position()

        # calculate new position
        if direction.lower() == 'w':
            new_position = (row - 1, col)

        elif direction.lower() == 'a':
            new_position = (row, col - 1)

        elif direction.lower() == 's':
            new_position = (row + 1, col)

        else:
            new_position = (row, col + 1)

        # check if wall
        maze = self.maze()
        if maze[new_position[0]][new_position[1]].is_blocking():
            return False

        return None


def main() -> None:
    pass


if __name__ == "__main__":
    main()
