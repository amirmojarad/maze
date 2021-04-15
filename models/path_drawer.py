# get path as deque, text_maze as raw map text
def draw(path, text_maze):
    # split raw text by whitespace ('\n) and make list by characters each line
    maze = text_maze.split()
    maze = [list(line) for line in maze]

    while len(path) > 0:
        node = path.pop()
        position = node.Position
        maze[position[0]][position[1]] = '@'

    maze = [''.join(line) for line in maze]
    maze = '\n'.join(maze)

    return maze
