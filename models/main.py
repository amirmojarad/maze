from map.map_generator import MapGenerator


def main():
    # reading maze from file
    print('Loading file...')
    with open('./example.txt') as file:
        text_maze = file.read()
    print('File loaded')

    print('Creating maze graph')
    maze_graph = MapGenerator(text_maze)
    print('Graph created')

    # TODO solve


if __name__ == '__main__':
    main()
