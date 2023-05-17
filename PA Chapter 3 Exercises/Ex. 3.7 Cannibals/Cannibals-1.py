from collections import deque
import time

class Agent:
    def solve(self, missionaries, cannibals):
        class States:
            def __init__(self, m_left, c_left, m_right, c_right, boat_pos):
                self.m_left = m_left
                self.c_left = c_left
                self.m_right = m_right
                self.c_right = c_right
                self.boat_pos = boat_pos
                self.parent = None

            def __eq__(self, x):
                return (self.m_left == x.m_left and self.c_left == x.c_left and
                        self.m_right == x.m_right and self.c_right == x.c_right and
                        self.boat_pos == x.boat_pos)

            
            def goal_state(self):
                if self.m_left == 0 and self.c_left == 0 and self.m_right == missionaries and self.c_right == cannibals and self.boat_pos == "right":
                    return True
                else:
                    return False

            def valid_state(self):
                if (self.m_left != 0 and self.c_left > self.m_left) or (self.m_right != 0 and self.c_right > self.m_right) \
                        or self.m_left < 0 or self.c_left < 0 or self.m_right < 0 or self.c_right < 0:
                    return False
                else:
                    return True

        def next_state(curr_state):
            result = []
            possible_moves = [(2, 0), (0, 2), (1, 1), (1, 0), (0, 1)]
            if curr_state.boat_pos == "left":  # boat moves from left to right
                for move in possible_moves:
                    new_state = States(curr_state.m_left - move[0], curr_state.c_left - move[1],
                                       curr_state.m_right + move[0], curr_state.c_right + move[1], "right")
                    if new_state.valid_state():
                        result.append(new_state)
                        new_state.parent = curr_state
            else:  # boat moves from right to left
                for move in possible_moves:
                    new_state = States(curr_state.m_left + move[0], curr_state.c_left + move[1],
                                       curr_state.m_right - move[0], curr_state.c_right - move[1], "left")
                    if new_state.valid_state():
                        result.append(new_state)
                        new_state.parent = curr_state
            return result

        def breadth_first_search():
            count=0
            initial_state = States(missionaries, cannibals, 0, 0, "left")  # root
            if initial_state.goal_state():
                return initial_state
            queue = deque([])
            explored = []
            queue.append(initial_state)
            while queue:
                node = queue.popleft()
                count+=1
                if node.goal_state():
                    return count, node
                explored.append(node)
                node_children = next_state(node)
                for child in node_children:
                    if (child not in explored) and (child not in queue):
                        queue.append(child)
            return count, None

        def find_moves(result):
            path = []
            final_path = []
            result_parent = result.parent
            while result_parent:
                move = (abs(result.m_left - result_parent.m_left),
                        abs(result.c_left - result_parent.c_left), result.m_left, result.c_left, result.m_right, result.c_right, result.boat_pos)
                path.append(move)
                result = result_parent
                result_parent = result.parent
            for i in range(len(path)):
                final_result = path[len(path) - 1 - i]
                final_path.append(final_result)
            return final_path

        count, solution = breadth_first_search()
        if solution:
            return count, find_moves(solution)
        else:
            return count, []

foo = Agent()
start=time.time()
count, sol = foo.solve(3, 3)
n=time.time()
execution_time=n-start
print("Initial State:\n"\
     "Missionaries Left: ", 3, "Cannibals Left: ", 3, "| Missionaries on boat:", 0, "Cannibals on boat:",\
         0, "| Missionaries Right: ", 0, "Cannibals Right: ", 0, "| Boat Pos: ", "left")

steps = 0
for i in sol:
    steps = steps + 1
    print("Step:", steps,  "\nMissionaries Left: ", i[2], "Cannibals Left: ", i[3], "| Missionaries on boat:", i[0], "Cannibals on boat:",\
         i[1], "| Missionaries Right: ", i[4], "Cannibals Right: ", i[5], "| Boat Pos: ", i[6])
print("\n")
print("Execution time: ", execution_time)
print("Performance measure: ", count)
            
            
