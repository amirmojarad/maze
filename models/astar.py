from FibonacciHeap import FibHeap
from priority_queue import FibPQ, HeapPQ, QueuePQ


# This implementatoin of A* is almost identical to the Dijkstra implementation. So for clarity I've removed all comments, and only added those
# Specifically showing the difference between dijkstra and A*

def solve(maze):
    # Width is used for indexing, total is used for array sizes
    width = maze.width
    total = maze.width * maze.height

    # Start node, end node
    start = maze.start
    startpos = start.Position
    end = maze.end
    endpos = end.Position

    # Visited holds true/false on whether a node has been seen already. Used to stop us returning to nodes multiple times
    visited = [False] * total
    # Previous holds a link to the previous node in the path. Used at the end for reconstructing the route
    prev = [None] * total

    # Distances holds the distance to any node taking the best known path so far. Better paths replace worse ones as we find them.
    # We start with all distances at infinity
    infinity = float("inf")
    distances = [infinity] * total

    # The priority queue. There are multiple implementations in priority_queue.py
    # unvisited = FibHeap()
    unvisited = HeapPQ()
    # unvisited = FibPQ()
    # unvisited = QueuePQ()

    # This index holds all priority queue nodes as they are created. We use this to decrease the key of a specific node when a shorter path is found.
    # This isn't hugely memory efficient, but likely to be faster than a dictionary or similar.
    nodeindex = [None] * total

    # To begin, we set the distance to the start to zero (we're there) and add it into the unvisited queue
    distances[start.Position[0] * width + start.Position[1]] = 0
    startnode = FibHeap.Node(0, start)
    nodeindex[start.Position[0] * width + start.Position[1]] = startnode
    unvisited.insert(startnode)

    # Zero nodes visited, and not completed yet.
    count = 0
    completed = False

    while len(unvisited) > 0:
        count += 1

        # Find current shortest path point to explore
        n = unvisited.removeminimum()

        # Current node u, all neighbours will be v
        u = n.value
        upos = u.Position
        uposindex = upos[0] * width + upos[1]

        if distances[uposindex] == infinity:
            break

        # If upos == endpos, we're done!
        if upos == endpos:
            completed = True
            break

        for v in u.Neighbours:
            if v is not None:
                vpos = v.Position
                vposindex = vpos[0] * width + vpos[1]

                if visited[vposindex] == False:
                    d = abs(vpos[0] - upos[0]) + abs(vpos[1] - upos[1])

                    # New path cost to v is distance to u + extra. Some descriptions of A* call this the g cost.
                    # New distance is the distance of the path from the start, through U, to V.
                    newdistance = distances[uposindex] + d

                    # A* includes a remaining cost, the f cost. In this case we use manhattan distance to calculate the distance from
                    # V to the end. We use manhattan again because A* works well when the g cost and f cost are balanced.
                    # https://en.wikipedia.org/wiki/Taxicab_geometry
                    remaining = abs(vpos[0] - endpos[0]) + abs(vpos[1] - endpos[1])

                    # Notice that we don't include f cost in this first check. We want to know that the path *to* our node V is shortest
                    if newdistance < distances[vposindex]:
                        vnode = nodeindex[vposindex]

                        if vnode is None:
                            # V goes into the priority queue with a cost of g + f. So if it's moving closer to the end, it'll get higher
                            # priority than some other nodes. The order we visit nodes is a trade-off between a short path, and moving
                            # closer to the goal.
                            vnode = FibHeap.Node(newdistance + remaining, v)
                            unvisited.insert(vnode)
                            nodeindex[vposindex] = vnode
                            # The distance *to* the node remains just g, no f included.
                            distances[vposindex] = newdistance
                            prev[vposindex] = u
                        else:
                            # As above, we decrease the node since we've found a new path. But we include the f cost, the distance remaining.
                            unvisited.decreasekey(vnode, newdistance + remaining)
                            # The distance *to* the node remains just g, no f included.
                            distances[vposindex] = newdistance
                            prev[vposindex] = u

        visited[uposindex] = True

    # We want to reconstruct the path. We start at end, and then go prev[end] and follow all the prev[] links until we're back at the start
    from collections import deque

    path = deque()
    current = end
    while current is not None:
        path.appendleft(current)
        x = current.Position[0] * width + current.Position[1]
        current = prev[current.Position[0] * width + current.Position[1]]

    return [path, [count, len(path), completed]]
