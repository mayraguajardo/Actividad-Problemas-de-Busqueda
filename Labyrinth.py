from simpleai.search import SearchProblem
from simpleai.search import astar

class Labyrinth(SearchProblem):
    def __init__(self, initial_state):
        super().__init__(initial_state=initial_state)
        self.xSize = len(initial_state)
        self.ySize = len(initial_state[0])
        print(f'Size {self.xSize} X {self.ySize}')
        print("Initial state:")
        Labyrinth.printLab(initial_state)
        print("")
    
    def actions(self, state):
        row, column = Labyrinth.find_point(state, '0')
        moves = []
        if row > 0:
            if Labyrinth.check_available(state, row-1, column):
                moves.append([row-1,column])
        if row < self.xSize-1:
            if Labyrinth.check_available(state, row+1, column):
                moves.append([row+1,column])
        if column > 0:
            if Labyrinth.check_available(state, row, column-1):
                moves.append([row,column-1])
        if column < self.ySize-1:
            if Labyrinth.check_available(state, row, column+1):
                moves.append([row,column+1])
        #print("row", row, "column", column)
        return moves
    
    def result(self, state, action):
        #print("actions", int(action[0]), action[1])
        row, column = Labyrinth.find_point(state, '0')
        new_move = state[action[0]][action[1]]
        state_list = list(list(state_tuple) for state_tuple in state)
        state_list[row][column] = '°'
        state_list[action[0]][action[1]] = '0'
        #print("")
        #Labyrinth.printLab(state)
        #print("")
        return tuple(tuple(s_list) for s_list in state_list)

    def is_goal(self, state):
        goal = not Labyrinth.has_X(state)
        #print(goal)
        if goal:
            print("Result:")
            Labyrinth.printLab(state)
        return goal
    
    def heuristic(self, state):
        distance = 0
        
        for row_goal, row in enumerate(self.initial_state):
            for col_goal, col in enumerate(row):
                row_current, col_current = Labyrinth.find_point(state, '0')

                distance += abs(row_current - row_goal) + abs(col_current - col_goal)

        return distance

    @staticmethod
    def find_point(state, point):
        for row in range(len(state)):
            for column in range(len(state[row])):
                if state[row][column] == point:
                    return (row, column)
        return (-1,-1)

    @staticmethod
    def check_available(state, row, column):
        if state[row][column] == ' ' or state[row][column] == 'X':
            return True
        else: return False

    @staticmethod
    def has_X(state):
        x, y = Labyrinth.find_point(state, 'X')
        #print(x, y)
        if x == -1:
            return False
        else: return True
    
    @staticmethod
    def printLab(state):
        for i in range(len(state)):
            for j in range(len(state[i])):
                print(state[i][j], end =" ")
            print("")

def print_pretty_path(path):
    for num, state in enumerate(path):
        print()
        if num == 0:
            print('Initial State:')
        else:
            print(f'Movement {num}:')
        Labyrinth.printLab(state[1])

def run(initial):
    print("_________________________")
    print('Starting Astar  Labyrinth ........')
    my_problem = Labyrinth(initial_state=initial)
    result_path = astar(my_problem, graph_search=True)
    print_pretty_path(result_path.path())
    print("Done")
    print("_________________________")

run((
    ('+', '+', '+', '+'),
    ('+', '0', ' ', '+'),
    ('+', ' ', '+', '+'),
    ('+', ' ', ' ', 'X'),
    ('+', '+', '+', '+')))

run((
    ('+','+','+','+','+','+','+','+','+','+','+','+','+','+','+','+','+'),
    ('+',' ','0','+',' ',' ',' ','+','+',' ','+','+',' ',' ',' ',' ','+'),
    ('+',' ',' ',' ',' ',' ','+',' ',' ',' ',' ',' ','+','+','+','+','+'),
    ('+',' ','+',' ',' ',' ',' ','+','+',' ',' ','+','+','+','+',' ','+'),
    ('+',' ','+',' ',' ',' ','+',' ','+',' ','+','+',' ',' ',' ',' ','+'),
    ('+',' ',' ',' ',' ',' ',' ',' ',' ','X',' ','+','+',' ',' ','+','+'),
    ('+','+','+','+','+','+','+','+','+','+','+','+','+','+','+','+','+')))

run((
    ('+','+','+','+','+','+','+','+','+','+','+','+','+','+','+','+','+','+','+','+','+','+'),
    ('+',' ','0','+',' ',' ',' ','+','+',' ','+','+',' ',' ',' ',' ',' ',' ',' ',' ',' ','+'),
    ('+',' ',' ',' ',' ',' ','+',' ',' ',' ',' ',' ','+','+','+','+','+','+','+',' ','+','+'),
    ('+',' ','+',' ',' ',' ',' ','+','+',' ',' ','+','+','+','+',' ','+','+','+',' ','+','+'),
    ('+',' ','+',' ',' ',' ','+',' ','+',' ','+','+',' ',' ',' ',' ',' ',' ',' ',' ',' ','+'),
    ('+',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','+','+',' ',' ','+','+',' ',' ','+',' ','+'),
    ('+','+','+','+','+',' ','+',' ','+',' ',' ',' ',' ',' ',' ','+','+',' ',' ','+',' ','+'),
    ('+','+','+','+','+',' ','+','+','+',' ',' ','+',' ','+',' ',' ','+','+',' ',' ',' ','+'),
    ('+',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','+',' ','+','X',' ','+',' ','+',' ',' ','+'),
    ('+','+','+','+','+',' ','+',' ',' ','+',' ','+',' ','+',' ',' ',' ',' ',' ',' ',' ','+'),
    ('+','+','+','+','+','+','+','+','+','+','+','+','+','+','+','+','+','+','+','+','+','+')))

#print(result_path.state)
#print(result_path.path())


