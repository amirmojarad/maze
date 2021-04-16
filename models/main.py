import map_generator
import astar
import path_drawer

import time


def main():
    # Reading maze from file
    print('Loading file...')
    with open('examples/normal.txt') as file:
        text_maze = file.read()
    print('File loaded')

    # Generate graph from raw text in file
    print('Creating maze graph')
    t1 = time.time()
    maze_graph = map_generator.MapGenerator(text_maze)
    t2 = time.time()
    print('Graph created in:', t2 - t1, 'seconds')
    print('nodes:', maze_graph.node_count)

    # Solve and fine path in maze by a* algorithm
    print('Start  solving maze')
    t1 = time.time()
    result = astar.solve(maze_graph)
    t2 = time.time()
    print('Maze solved in:', t2 - t1, 'seconds')

    print('node visited:', result.get('node_visited'))
    print('path length:', result.get('path_length'))
    print('path founded:', result.get('completed'))

    solved = path_drawer.draw(result.get('path'), text_maze)
    with open('answer.txt', 'w') as file:
        file.write(solved)


if __name__ == '__main__':
    main()
