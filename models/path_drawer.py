def draw(path, text_maze):
    maze = text_maze.split()
    maze = [list(line) for line in maze]

    while len(path) > 0:
        node = path.pop()
        position = node.Position
        maze[position[0]][position[1]] = '@'

    maze = [''.join(line) for line in maze]
    maze = '\n'.join(maze)

    return maze
