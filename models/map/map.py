class MazeMap:

    def __init__(self, width, height, maze_map) -> None:
        super().__init__()
        # initial maze_map
        self._width = width
        self._height = height
        self._maze_map = maze_map

    def get_maze_map(self):
        return self._maze_map

    def get_width(self):
        return self._width

    def get_height(self):
        return self._height

    def set_maze_map(self, maze_map):
        self._maze_map = maze_map
