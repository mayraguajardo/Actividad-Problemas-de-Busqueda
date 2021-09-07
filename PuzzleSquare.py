from simpleai.search import SearchProblem
from simpleai.search import astar
import time

class PuzzleSquare(SearchProblem):
    def __init__(self, initial_state):
        super().__init__(initial_state=initial_state)
        self.goal = PuzzleSquare.get_goal(initial_state)
        self.size = len(self.goal)
        print(f'Size {self.size} X {self.size}')


    def actions(self, state):
        row, column = PuzzleSquare.find_number(state, 0)
        moves = []
        if row > 0:
            moves.append([row-1,column])
        if row < self.size-1:
            moves.append([row+1,column])
        if column > 0:
            moves.append([row,column-1])
        if column < self.size-1:
            moves.append([row,column+1])
        
        return moves

    def result(self, state, action):
        row, column = PuzzleSquare.find_number(state, 0)
        moved_number = state[action[0]][action[1]]
        state_list = list(list(state_tuple) for state_tuple in state)
        state_list[row][column] = moved_number
        state_list[action[0]][action[1]] = 0
        return tuple(tuple(s_list) for s_list in state_list)

    def is_goal(self, state):
        return state == self.goal
    
    def cost(self, state, action, state2):
        return 1

    def heuristic(self, state):
        distance = 0

        for row_goal, row in enumerate(self.goal):
            for col_goal, col in enumerate(row):
                target_num = self.goal[row_goal][col_goal]
                row_current, col_current = PuzzleSquare.find_number(state,target_num)

                distance += abs(row_current - row_goal) + abs(col_current - col_goal)

        return distance

    @staticmethod
    def find_number(state, number):
        for row in range(len(state)):
            for column in range(len(state)):
                if state[row][column] == number:
                    return (row, column)

    @staticmethod
    def get_goal(state):
        rows = len(state)
        columns = len(state[0])

        if rows != columns:
            raise ValueError('List must be square')

        goal_number = 0
        list_goal = []
        for i in range(rows):
            row = []
            for j in range(columns):
                row.append(goal_number)
                goal_number+=1
            list_goal.append(tuple(row))
        goal = tuple(list_goal)
        return goal

def print_square(state):
    print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
      for row in state]))

def print_preety_path(path):
    for num, state in enumerate(path):
        print()
        if num == 0:
            print('Initial State:')
        else:
            print(f'Movement {num}:')
        print_square(state[1])



# my_problem = PuzzleSquare(initial_state=((1,8,2),(0,4,3),(7,6,5)))
# tic = time.perf_counter()
# result = astar(my_problem)
# toc = time.perf_counter()
# print('\nPuzzle 3x3 ---\n')
# print_square(result.state)
# print_preety_path(result.path())
# print(f"Duration: {toc - tic:0.4f} seconds")

my_problem = PuzzleSquare(initial_state=((1,2,3,7),(4,5,6,0),(8,9,10,11),(12,13,14,15)))
tic = time.perf_counter()
result = astar(my_problem)
toc = time.perf_counter()
print('\nPuzzle 4x4 ---\n')
print_square(result.state)
print_preety_path(result.path())
print(f"Duration: {toc - tic:0.4f} seconds")

