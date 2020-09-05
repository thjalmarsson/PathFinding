"""
First algorithm to be implemented will be BFS
1. The maze will be represented by a matrix
2. Starting point will be S
3. Goal will be F
4. visited paths will be +
5. walls will be X
6. Final path will be "P"
7. Unvisited nodes will be 0

BFS works as follows:
Visit all neighbors that hasent been visited
then visit their neighbours etc

Will implement this with a queue
"""
import queue


#S = (2,2)
maze1 = [["X","X","X","X","X","X","X","X","X","X"],
		["X","O","O","O","O","O","O","O","O","X"],
		["X","O","S","O","O","O","O","O","O","X"],
		["X","O","O","O","O","O","O","O","O","X"],
		["X","O","O","O","O","O","O","O","O","X"],
		["X","O","O","O","O","O","O","O","O","X"],
		["X","O","O","O","O","O","O","F","O","X"],
		["X","X","X","X","X","X","X","X","X","X"]]

"""
Functions that we are going to need
1. valid_node() Check if the next step is a valid step i.e not a wall or not a previously visited node [Done]
2. move_node() that steps in a direction (going to call them up, down, left ,right), going to use a string to 
	represent these, Up = "U", Left = "L", Down = "D", Right = "R"
"""

def valid_node(maze,moves, row, col):
	new_row = row
	new_col = col
	for move in moves:
		if move == "U":
			new_row = row - 1
		elif move == "D":
			new_row = row + 1
		elif move == "L":
			new_col = col - 1
		elif move == "R":
			new_col = col + 1

	if maze[new_row][new_col] == "X":
		return False
	elif maze[new_row][new_col] == "+":
		return False
	elif maze[new_row][new_col] == "S":
		return False
	else:
		return True

def finish_node(maze, row, col):
	if maze[row][col] == "F":
		return True
	else:
		return False

def move_node(maze, moves, row, col):
	new_row = row
	new_col = col
	for move in moves:
		if move == "U":
			new_row = row - 1
			maze[new_row][new_col] = "+"
		elif move == "D":
			new_row = row + 1
			maze[new_row][new_col] = "+"
		elif move == "L":
			new_col = col - 1
			maze[new_row][new_col] = "+"
		elif move == "R":
			new_col = col + 1
			maze[new_row][new_col] = "+"

def print_maze(maze):
	for row in maze:
		print(row)

def print_queue(q):
	for n in list(q.queue):
		print(n)

"""
queue.put(n) adds n to the end of the queue
n = queue.get() takes the first element from the queue and stores it in n
"""

directions = "URDL"

q = queue.Queue()
for direction in directions:
	q.put(direction)

current_row = 2
current_col = 2

# Here I am implementing the main loop to search through the grid
"""
while not finish_node(maze1, current_row, current_col):
	for direction in directions:
		my_queue.put(direction)

"""



"""
for direction in directions:
	my_queue.put(direction)
print_queue(my_queue)
"""

"""

new_test_row, new_test_col = move_node(maze1, "L", old_test_row, old_test_col)
print(maze1[new_test_row][new_test_col])
"""
old_test_row = 2
old_test_col = 2
new_test_row, new_test_col = move_node(maze1, "L", old_test_row, old_test_col)
print_maze(maze1)