class MapGenerator:
    """"
    MapGenerator
        this class generate maze_map
    """
    class Node:
        """
        keeps position and neighbors of a node
        """
        def __init__(self, position):
            # tuple: (y ,x)
            #     height, width
            self.Position = position
            #                 above/right/below/left
            self.Neighbours = [None, None, None, None]

        def __lt__(self, other) -> bool:
            return True

    def __init__(self, raw_map):
        self.node_count = 0
        lines = raw_map.split()

        self.width = len(lines[0])
        self.height = len(lines)

        self.start = None
        self.end = None

        # making graph
        # saving top nodes of each hallway
        top_nodes = [None] * self.width

        # find end node
        for x in range(1, self.width - 1):
            # if node is the end node
            if lines[0][x] == 'G':
                self.end = MapGenerator.Node((0, x))
                top_nodes[x] = self.end
                self.node_count += 1
                break

        # find middle nodes
        for y in range(1, self.height - 1):
            # set previous, current and next node status
            prv = False
            cur = False
            # check if next node is path or not
            nxt = True if lines[y][1] == '-' else False

            # keep left node details
            leftnode = None

            for x in range(1, self.width - 1):
                # print('y, x:', y, x)  # TODO DEBUG
                # move prev, current and next onwards
                prv = cur
                cur = nxt
                nxt = True if lines[y][x + 1] == '-' else False

                n = None

                if cur == False:
                    # current on wall - continue
                    continue

                if prv == True:
                    if nxt == True:
                        # PATH PATH PATH
                        # create node if paths above or below
                        if lines[y - 1][x] == '-' or lines[y + 1][x] == '-' or lines[y - 1][x] == 'G' or lines[y + 1][x] == 'S':
                            n = MapGenerator.Node((y, x))
                            leftnode.Neighbours[1] = n
                            n.Neighbours[3] = leftnode
                            leftnode = n
                    else:
                        # PATH PATH WALL
                        # create node at end of hallway
                        n = MapGenerator.Node((y, x))
                        leftnode.Neighbours[1] = n
                        n.Neighbours[3] = leftnode
                        leftnode = None
                else:
                    if nxt == True:
                        # WALL PATH PATH
                        # Create node at start of hallway
                        n = MapGenerator.Node((y, x))
                        leftnode = n
                    else:
                        # WALL PATH WALL
                        # Create node only if in dead end
                        if lines[y - 1][x] == '%' or lines[y + 1][x] == '%':
                            n = MapGenerator.Node((y, x))

                # if node was initialized
                if n is not None:
                    print('node', n.Position)  # TODO DEBUG
                    # Clear above, connect to waiting top node
                    if lines[y - 1][x] == '-' or lines[y - 1][x] == 'G':
                        t = top_nodes[x]
                        t.Neighbours[2] = n
                        n.Neighbours[0] = t

                    # If clear below, put this new node in the top row for the next connection
                    if lines[y + 1][x] == '-' or lines[y + 1][x] == 'S':
                        top_nodes[x] = n
                    else:
                        top_nodes[x] = None

                    self.node_count += 1

        # find start node
        y = self.height - 1
        for x in range(1, self.width - 1):
            if lines[y][x] == 'S':
                self.start = MapGenerator.Node((self.height - 1, x))
                t = top_nodes[x]
                t.Neighbours[2] = self.start
                self.start.Neighbours[0] = t
                self.node_count += 1
                break
