from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

class Graph:
    def __init__(self):
        self.visited = {}


    def bfs(self,starting_room):
        traveled_path = []
            
        queue = Queue()

        visited = set()

        queue.enqueue([starting_room])

        while queue.size() > 0:

            path = queue.dequeue()

            current_room = path[-1]

            if current_room is destination_room:
            # if so, return path
                return path


            if current_room not in visited:
                visited.add(current_room)

                neighboring_rooms = visited_graph[current_room]

                for room in neighboring_rooms:
                    new_path = list(path)
                    new_path.append(visited_graph[current_room][room])
                    queue.enqueue(new_path)
                    # print('roo',visited_graph[current_room][room])

        return traveled_path


    def dft(self, starting_room):

        stack = Stack()

        # visited = {}

        previous_room = None

        stack.push(starting_room)

        while stack.size() > 0:
            current_room = stack.pop()
            player.current_room = current_room

            # print('current_room', current_room)
            # print('previous_room',previous_room)

            if current_room.id not in self.visited:

                exit_dict = {}

                exits = current_room.get_exits()


                for ex in exits:
                    exit_dict[ex] = '?'

                self.visited[current_room.id] = exit_dict
                # print('visited before', self.visited)
                for vis in self.visited:
                    # print(vis)
                    for d in self.visited[vis]:
                        # print(d)
                        if self.visited[vis][d] == current_room.id and vis == previous_room:
                            a = None
                            if d == 'n':
                                a = 's'
                            if d == 'n':
                                a = 's'
                            if d == 'e':
                                a = 'w'
                            if d == 'w':
                                a = 'e'
                            traversal_path.append(d)
                            self.visited[current_room.id][a] = previous_room

                # print('visited after', self.visited)
                temp_diretions = set()
                for emp in self.visited[current_room.id]:
                    # print(self.visited[current_room.id][emp])
                    temp_diretions.add(self.visited[current_room.id][emp])
                # print('temp_diretions', temp_diretions)
                if '?' not in temp_diretions:
                    return current_room
                    break
                for e in exits:
                    player.travel(f'{e}')
                    next_room = player.current_room
                    self.visited[current_room.id][f'{e}'] = next_room.id
                    if e == 'n':
                        player.travel('s')
                    if e == 's':
                        player.travel('n')
                    if e == 'e':
                        player.travel('w')
                    if e == 'w':
                        player.travel('e')
                    stack.push(next_room)
                previous_room = current_room.id
                    
        # return self.visited
    
    def traveling(self, starting_node):
        room = self.dft(starting_node)



graph = Graph()

visit = graph.traveling(world.starting_room)
# travel = graph.bfs(visit, world.starting_room.id)
# traversal_path = visit
print('traversal_path',traversal_path)
print(visit)

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
