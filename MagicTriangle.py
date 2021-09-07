from simpleai.search import SearchProblem
from simpleai.search import breadth_first
from simpleai.search import depth_first
import time

GOAL = 10
NUMBERS = [1,2,3,4,5,6]


class MagicTriangleProblem(SearchProblem):
    def actions(self, state):
        set_difference = set(NUMBERS) - set(state)
        list_difference = list(set_difference)
        return list_difference

    def result(self, state, action):
        state_list = list(state)
        next_empty = state_list.index(0)
        state_list[next_empty] = action
        return tuple(state_list)

    def is_goal(self, state):
        side1 = state[0] + state[1] + state[2]
        side2 = state[2] + state[3] + state[4]
        side3 = state[4] + state[5] + state[0]
        return side1 == GOAL and side2 == GOAL and side3 == GOAL and (0 not in state)
    
    def cost(self, state, action, state2):
        return 1

def print_triangle(tuple):
    print(f'  {tuple[0]}  ')
    print(f' {tuple[1]} {tuple[5]} ')
    print(f'{tuple[2]} {tuple[3]} {tuple[4]}')


my_problem = MagicTriangleProblem(initial_state=(0,0,0,0,0,0))
tic = time.perf_counter()
result_depth_first = depth_first(my_problem)
toc = time.perf_counter()
print('Depth First---')
print(print_triangle(result_depth_first.state))
print(result_depth_first.path())
print(f"Duration: {toc - tic:0.4f} seconds")


print()

tic = time.perf_counter()
result_breadth_first = breadth_first(my_problem)
toc = time.perf_counter()
print('Breadth First---')
print(print_triangle(result_breadth_first.state))
print(result_breadth_first.path())
print(f"Duration: {toc - tic:0.4f} seconds")