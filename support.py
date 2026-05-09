Maze = list[list['Tile']]
Position = tuple[int, int]

# Tile constants
TILE = 'T'
WALL = 'W'
FLOOR = ' '
GOAL = 'G'
FILLED_GOAL = 'X'

# Entity constants
ENTITY = 'E'
CRATE = 'C'
PLAYER = 'P'
POTION = 'O'
STRENGTH_POTION = 'S'
MOVE_POTION = 'M'
FANCY_POTION = 'F'

# Effect constants
STRENGTH = 'strength'
MOVE = 'moves'

# Movement constants
UP = 'w'
DOWN = 's'
LEFT = 'a'
RIGHT = 'd'
QUIT = 'q'

DIRECTION_DELTAS = {
    UP: (-1, 0),
    DOWN: (1, 0),
    LEFT: (0, -1),
    RIGHT: (0, 1),
}

# Display constants
MOVE_PROMPT = 'Enter move (or `q` to quit): '
WIN_MSG = 'You Won!'
LOSE_MSG = 'You lost!'
INVALID_MSG = 'Invalid move\n'


def display_game(
    maze: Maze,
    entity_positions: dict[Position,'Entity'],
    player: 'Player'
) -> None:
    """ Display the current state of the game.
    
    Parameters:
        maze (Maze): The current maze.
        entity_positions (dict[Position,Entity]): Map of positions to entities 
                currently present.
        player (Player): The current player entity.
    """
    # Maze
    for i, row in enumerate(maze):
        for j, tile in enumerate(row):
            if (i, j) == player.get_position():
                print(PLAYER, end='')
            else:
                print(entity_positions.get((i, j), tile), end='')
        print()

    # Stats
    moves = player.get_moves_remaining()
    strength = player.get_strength()
    print(f'\nMoves remaining: {moves}, strength: {strength}\n')
    