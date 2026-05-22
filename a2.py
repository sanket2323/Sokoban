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
        """Initialize a tile.
        Returns:
            None.
        """
        pass

    def __str__(self) -> str:
        """Return the string representation of the tile.
        Returns:
            String.
        """
        return TILE

    def __repr__(self) -> str:
        """
        Return the string of the tile.
        Returns:
            String
        """
        return "Tile()"

    def get_type(self) -> str:
        """
        Return the type of the tile.
        Returns:
            The tile type.
        """
        return TILE

    def is_blocking(self) -> bool:
        """
        Check whether the tile blocks movement.
        Returns:
            True if the tile blocks movement, otherwise False.
        """
        return False


# task 2
class Floor(Tile):
    def __init__(self):
        """Initialize a tile.
        Returns:
            None.
        """
        super().__init__()

    def __repr__(self) -> str:
        """Return the official string representation of the floor tile.
        Returns:
        The floor tile representation.
        """
        return "Floor()"

    def __str__(self) -> str:
        """
        Return the string representation of the floor tile.

        Returns:
            The floor tile character.
        """
        return FLOOR

    def get_type(self) -> str:
        """
        Return the type of the floor tile.
        Returns:
            The floor tile type.
        """
        return FLOOR


# task 3
class Wall(Tile):
    def __init__(self):
        """
        Initialize a wall tile.
        Returns:
            None.
        """
        super().__init__()

    def __repr__(self) -> str:
        """
        Return the official string representation of the wall tile.

        Returns:
            The wall tile representation.

        """
        return "Wall()"

    def __str__(self) -> str:
        """
        Return the string representation of the wall tile.
        Returns:
            The wall tile character.
        """
        return WALL

    def get_type(self) -> str:
        """
        Return the type of the wall tile.
        Returns:
            The wall tile type.
        """
        return WALL

    def is_blocking(self) -> bool:
        """
        Check whether the wall blocks movement.
        Returns:
            True because walls block movement.
        """
        return True


# task 4
class Goal(Tile):
    def __init__(self):
        """
        Initialize a goal tile.
        Returns:
            None.
        """
        self.is_filled_or_not = False

    def __str__(self) -> str:
        """
        Return the string representation of the goal tile.
        Returns:
            The goal tile character.
        """
        if not self.is_filled_or_not:
            return GOAL
        else:
            return FILLED_GOAL

    def __repr__(self) -> str:
        """
        Return the official string representation of the goal tile.
        Returns:
            The goal tile representation.
        """
        return "Goal()"

    def is_filled(self) -> bool:
        """
        Check whether the goal is filled.
        Returns:
            True if the goal is filled, otherwise False.
        """

        return self.is_filled_or_not

    def fill(self):
        """
        Fill the goal tile.
        Returns:
            None.

        """
        self.is_filled_or_not = True

    def unfill(self):
        """
        Unfill the goal tile.
        Returns:
            None.
        """
        self.is_filled_or_not = False

    def get_type(self) -> str:
        """
        Return the type of the goal tile.
        Returns:
            The goal tile type.
        """
        return GOAL


# task 5
class Entity:
    def __init__(self, position: Position):
        """
        Initialize an entity.
        Parameters:
            position: Position of the entity.

        Returns:
            None.
        """
        self.position = position

    def __str__(self) -> str:
        """
        Return the string representation of the entity.
        Returns:
            The entity character.
        """
        return ENTITY

    def __repr__(self) -> str:
        """
        Return the official string representation of the entity.
        Returns:
            The entity representation.
        """
        x = self.position[0]
        y = self.position[1]
        return f"Entity(({x}, {y}))"

    def get_type(self) -> str:
        """
        Return the type of the entity.
        Returns:
            The entity type.
        """
        return ENTITY

    def get_position(self) -> Position:
        """
        Return the entity position.
        Returns:
            The entity position.
        """
        return self.position

    def set_position(self, new_pos: Position):
        """
        Update the entity position.

        Parameters:
            new_pos: New position of the entity.

        Returns:
            None.
        """
        self.position = new_pos


# task 6
class Potion(Entity):
    def __init__(self, position):
        """
        Initialize a potion.
        Parameters:
            position: Position of the potion.
        Returns:
            None.
        """
        super().__init__(position)

    def __str__(self) -> str:
        """
        Return the string representation of the potion.
        Returns:
            The potion character.
        """
        return POTION

    def __repr__(self) -> str:
        """
        Return the official string representation of the potion.

        Returns:
            The potion representation.
        """
        x = self.position[0]
        y = self.position[1]
        return f"Potion(({x}, {y}))"

    def get_type(self) -> str:
        """
        Return the type of the potion.

        Returns:
            The potion type.
        """
        return POTION

    def effect(self):
        """
        Return the potion effect.

        Returns:
            A dictionary containing potion effects.
        """
        return {}


# task 7
class StrengthPotion(Potion):
    def __init__(self, position):
        """
        Initialize a strength potion.

        Parameters:
            position: Position of the potion.

        Returns:
            None.
        """
        super().__init__(position)

    def __str__(self) -> str:
        """
        Return the string representation of the strength potion.

        Returns:
            The strength potion character.
        """
        return STRENGTH_POTION

    def __repr__(self) -> str:
        """
        Return the official string representation of the strength potion.

        Returns:
            The strength potion representation.
        """
        x = self.position[0]
        y = self.position[1]
        return f"StrengthPotion(({x}, {y}))"

    def get_type(self) -> str:
        """
        Return the type of the strength potion.

        Returns:
            The strength potion type.
        """
        return STRENGTH_POTION

    def effect(self):
        """
        Return the strength potion effect.

        Returns:
            A dictionary containing strength effects.
        """
        return {
            'strength': 2
        }


# task 8
class MovePotion(Potion):
    def __init__(self, position):
        """
        Initialize a move potion.

        Parameters:
            position: Position of the potion.

        Returns:
            None.
        """
        super().__init__(position)

    def __str__(self) -> str:
        """
        Return the string representation of the move potion.

        Returns:
            The move potion character.
        """
        return MOVE_POTION

    def __repr__(self) -> str:
        """
        Return the official string representation of the move potion.

        Returns:
            The move potion representation.
        """
        x = self.position[0]
        y = self.position[1]
        return f"MovePotion(({x}, {y}))"

    def get_type(self) -> str:
        """
        Return the type of the move potion.

        Returns:
            The move potion type.
        """
        return MOVE_POTION

    def effect(self):
        """
        Return the move potion effect.

        Returns:
            A dictionary containing move effects.
        """
        return {
            'moves': 5
        }


# task 9
class FancyPotion(Potion):
    def __init__(self, position):
        """
        Initialize a fancy potion.

        Parameters:
            position: Position of the potion.

        Returns:
            None.
        """
        super().__init__(position)

    def __str__(self) -> str:
        """
        Return the string representation of the fancy potion.

        Returns:
            The fancy potion character.
        """
        return FANCY_POTION

    def __repr__(self) -> str:
        """
        Return the official string representation of the fancy potion.

        Returns:
            The fancy potion representation.
        """
        x = self.position[0]
        y = self.position[1]
        return f"FancyPotion(({x}, {y}))"

    def get_type(self) -> str:
        """
        Return the type of the fancy potion.

        Returns:
            The fancy potion type.
        """

        return FANCY_POTION

    def effect(self):
        """
        Return the fancy potion effect.

        Returns:
            A dictionary containing potion effects.
        """
        return {
            'strength': 2,
            'moves': 2
        }


# task 10
class Crate(Entity):

    def __init__(self, position, weight):
        """
        Initialize a crate.

        Parameters:
            position: Position of the crate.
            weight: Weight of the crate.

        Returns:
            None.
        """
        super().__init__(position)
        self.weight = weight

    def __str__(self):
        """
        Return the string representation of the crate.

        Returns:
            The crate weight as a string.
        """
        return str(self.weight)

    def __repr__(self) -> str:
        """
        Return the official string representation of the crate.

        Returns:
            The crate representation.
        """
        x = self.position[0]
        y = self.position[1]
        z = self.weight
        return f"Crate(({x}, {y}), {z})"

    def get_weight(self):
        """
        Return the crate weight.

        Returns:
            The crate weight.
        """
        return self.weight

    def get_type(self) -> str:
        """
        Return the type of the crate.

        Returns:
            The crate type.
        """
        return CRATE


# task 11
class Player(Entity):

    def __init__(self, position: Position, strength: int, moves_remaining: int):
        """
        Initialize a player.

        Parameters:
            position: Position of the player.
            strength: Player strength value.
            moves_remaining: Remaining player moves.

        Returns:
            None.

        """
        super().__init__(position)
        self.strength = strength
        self.moves_remaining = moves_remaining

    def __str__(self):
        """
        Return the string representation of the player.

        Returns:
            The player character.

        """
        return PLAYER

    def __repr__(self) -> str:
        """
        Return the official string representation of the player.

        Returns:
            The player representation.
        """
        w = self.position[0]
        x = self.position[1]
        y = self.strength
        z = self.moves_remaining
        return f"Player(({w}, {x}), {y}, {z})"

    def get_type(self) -> str:
        """
        Return the type of the player.

        Returns:
            The player type.
        """
        return PLAYER

    def get_strength(self) -> int:
        """
        Return the type of the player.

        Returns:
            The player type.
        """
        return self.strength

    def add_strength(self, strength):
        """
        Increase the player's strength.

        Parameters:
            strength: Strength value to add.

        Returns:
            None.
        """
        self.strength += strength

    def get_moves_remaining(self) -> int:
        """
        Return the player's remaining moves.

        Returns:
            The number of remaining moves.
        """
        return self.moves_remaining

    def add_moves_remaining(self, moves):
        """
        Increase the player's remaining moves.

        Parameters:
            moves: Number of moves to add.

        Returns:
            None.
        """
        self.moves_remaining += moves

    def apply_effect(self, potion_effect):
        """
        Apply a potion effect to the player.

        Parameters:
            potion_effect: Dictionary containing potion effects.

        Returns:
            None.

        """
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
    """
    Read a maze file and create game objects.

    Parameters:
        maze_file: Name of the maze file.

    Returns:
        A tuple containing the maze, entities, and player.
    """
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
        """
        Initialize the Sokoban model.

        Parameters:
            maze: Maze grid for the game.
            entities: List of game entities.
            player: Player object.

        Returns:
            None.

        """
        self.maze = maze
        self.entities = entities
        self.player = player

    def get_maze(self) -> Maze:
        """
        Return the maze.

        Returns:
            The maze grid.
        """
        return self.maze

    def get_entities(self) -> list[Entity]:
        """
        Return the game entities.

        Returns:
            A list of entities.
        """
        return self.entities

    def get_player(self):
        """
        Return the player object.

        Returns:
            The player.
        """
        return self.player

    def entity_positions(self) -> dict[Position, Entity]:
        """
        Create a dictionary of entity positions.

        Returns:
            A dictionary mapping positions to entities.
        """
        position_dict = {}
        for entity in self.entities:
            position_dict[entity.get_position()] = entity
        return position_dict

    def has_won(self) -> bool:
        """
        Check whether the player has won the game.

        Returns:
            True if all goals are filled, otherwise False.
        """
        for row in self.maze:
            for tile in row:
                if tile.get_type() == GOAL and not tile.is_filled():
                    return False
        return True

    def has_lost(self) -> bool:
        """
        Check whether the player has lost the game.

        Returns:
            True if the player has no remaining moves, otherwise False.
        """
        if self.player.get_moves_remaining() <= 0 and not self.has_won():
            return True
        return False

    def shove_crate(self, crate, direction) -> bool:
        """
        Attempt to move a crate in a direction.

        Parameters:
            crate: Crate to move.
            direction: Direction of movement.

        Returns:
            True if the crate moves successfully, otherwise False.
        """

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
        """
        Attempt to move the player in a direction.

        Parameters:
            direction: Direction for player movement.

        Returns:
            True if the move succeeds, otherwise False.
        """
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

        # check if wall is blocking
        maze = self.get_maze()
        if maze[new_position[0]][new_position[1]].is_blocking():
            return False

        # check if entity is blocking
        entity_position = self.entity_positions()

        if new_position in entity_position:

            entity_type = entity_position[new_position]

            # crate handling
            if entity_type.get_type() == CRATE:
                # push the crate

                if not self.shove_crate(entity_type, direction):
                    return False

            # potion handling
            else:
                self.player.apply_effect(entity_type.effect())
                self.entities.remove(entity_type)

        # move player
        self.player.set_position(new_position)

        # subtract moves
        self.player.add_moves_remaining(-1)
        return True


# task 14
class Sokoban:
    def __init__(self, maze_file: str):
        maze, entities, player = read_file(maze_file)


def main() -> None:
    pass


if __name__ == "__main__":
    main()
