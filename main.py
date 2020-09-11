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


maze2 = [["X","X","X","X","X","X","X","X","X","X"],
		["X","O","O","X","O","O","O","O","O","X"],
		["X","O","S","X","O","O","O","O","O","X"],
		["X","O","O","X","O","X","X","X","O","X"],
		["X","O","O","X","O","X","O","O","O","X"],
		["X","O","O","X","O","X","O","O","O","X"],
		["X","O","O","O","O","X","O","F","O","X"],
		["X","X","X","X","X","X","X","X","X","X"]]

"""
Functions that we are going to need
1. valid_node() Check if the next step is a valid step i.e not a wall or not a previously visited node [Done]
2. move_node() that steps in a direction (going to call them up, down, left ,right), going to use a string to 
	represent these, Up = "U", Left = "L", Down = "D", Right = "R"
"""
# checks if the path is valid
def valid_node(maze,moves, row, col):
	new_row = row
	new_col = col
	for move in moves:
		if move == "U":
			new_row = new_row - 1
		elif move == "D":
			new_row = new_row + 1
		elif move == "L":
			new_col = new_col - 1
		elif move == "R":
			new_col = new_col + 1

	if maze[new_row][new_col] == "X":
		return False
	elif maze[new_row][new_col] == "+":
		return False
	elif maze[new_row][new_col] == "S":
		return False
	else:
		return True
# Returns true if its the "goal node"
def finish_node(maze, row, col):
	if maze[row][col] == "F":
		current_row, current_col = move_node(maze, current_path, starting_row, starting_col, "0")
		return True
	else:
		return False

# Takes a list of moves then sets those moves to +
def move_node(maze, moves, row, col, symbol):
	new_row = row
	new_col = col
	for move in moves:
		if move == "U":
			new_row = new_row - 1
			if maze[new_row][new_col] != "F":
				maze[new_row][new_col] = symbol
		elif move == "R":
			new_col = new_col + 1
			if maze[new_row][new_col] != "F":
				maze[new_row][new_col] = symbol
		elif move == "L":
			new_col = new_col - 1
			if maze[new_row][new_col] != "F":
				maze[new_row][new_col] = symbol
		elif move == "D":
			new_row = new_row + 1
			if maze[new_row][new_col] != "F":
				maze[new_row][new_col] = symbol
	return new_row, new_col

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


starting_row = 2
starting_col = 2
current_row = 2
current_col = 2
current_path = ""
# Here I am implementing the main loop to search through the grid
while not finish_node(maze2, current_row, current_col):
	current_path = q.get()
	if valid_node(maze2, current_path, starting_row, starting_col):
		current_row, current_col = move_node(maze2, current_path, starting_row, starting_col, "+")
		print("row: " + str(current_row) + ", col: " + str(current_col))
		for direction in directions:
			q.put(current_path + direction)

print_maze(maze2)
print("Finished at row: " + str(current_row) + " and col: " + str(current_col) + " with path: " + current_path)
#Problemet nu är att den markerar målnoden som + och därav inte känner av att den ska bryta
