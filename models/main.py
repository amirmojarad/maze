from map.map_generator import MapGenerator
import astar
import time


def main():
    # reading maze from file
    print('Loading file...')
    with open('./example.txt') as file:
        text_maze = file.read()
    print('File loaded')

    print('Creating maze graph')
    t1 = time.time()
    maze_graph = MapGenerator(text_maze)
    t2 = time.time()
    print('Graph created in:', t2 - t1)

    t1 = time.time()
    solved = astar.solve(maze_graph)
    t2 = time.time()
    print('Maze solved in:', t2 - t1)

    print(solved[1])
    print(solved[0])


if __name__ == '__main__':
    main()
