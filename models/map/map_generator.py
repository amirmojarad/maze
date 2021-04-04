""""
MapGenerator
    this class generate maze_map
"""
from models.map.map import MazeMap


class MapGenerator:
    def __init__(self, raw_map) -> None:
        super().__init__()
        self._raw_map = raw_map
        self._lines = []

    def _get_lines(self):
        return self._raw_map.split("\n")

    def get_map(self):
        result_map = [[] for x in range(0, 5)]
        self._lines = self._get_lines()
        # get width of map in first character of raw map
        width = self._lines[0][0]
        # get width of map in third character of raw map
        height = self._lines[0][2]
        # then remove first line (WIDTH,HEIGHT)
        self._lines.pop(0)
        index = 0
        for l in self._lines:
            result_map[index] = list(l)
            index += 1
        maze = MazeMap(width, height, result_map)
        return maze
