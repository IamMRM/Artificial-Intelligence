import sys
from simpleai.search import SearchProblem, breadth_first, depth_first,limited_depth_first, iterative_limited_depth_first, uniform_cost

'''
8 puzzle problem, a smaller version of the fifteen puzzle:
http://en.wikipedia.org/wiki/Fifteen_puzzle
States are defined as string representations of the pieces on the puzzle.
Actions denote what piece will be moved to the empty space.
States must allways be inmutable. We will use strings, but internally most of
the time we will convert those strings to lists, which are easier to handle.
For example, the state (string):
'1-2-3
 4-5-6
 7-8-e'
will become (in lists):
[['1', '2', '3'],
 ['4', '5', '6'],
 ['7', '8', 'e']]
'''
from timeit import default_timer as timer
from simpleai.search import * 
'''
SearchProblem, breadth_first, depth_first, limited_depth_first, iterative_limited_depth_first, uniform_cost'''

GOAL = '''Bucharest'''
INITIAL = '''Arad'''
graph = {"Oradea": {
                "Zerind": 71,
                "Timisoara": 118
            }
 ,"Arad": {
                "Sibiu": 140,
                "Timisoara": 118,
                "Zerind":75
            }
 ,"Zerind": {
                "Oradea": 70,
                "Arad": 75
            }
 ,"Sibiu": {
                "Arad": 140,
                "Oradea": 151,
                "Fagaras":99,
                "Rimnicu Vilcea":80
            }
 ,"Fagaras": {
                "Sibiu": 99,
                "Bucharest": 211
            }
 ,"Rimnicu Vilcea": {
                "Sibiu": 80,
                "Pitesti": 97,
                "Craiova":146
            }
 ,"Timisoara": {
                "Arad": 118,
                "Lugoj": 111
                }
  ,"Lugoj": {
                "Timisoara": 111,
                "Mehadia": 70
                }
 ,"Mehadia": {
                "Lugoj": 70,
                "Drobeta": 74
                }
 ,"Drobeta": {
                "Mehadia": 75,
                "Craiova": 120
                }
  ,"Craiova": {
                "Drobeta": 120,
                "Rimnicu Vilcea": 146,
                "Pitesti": 138
                }
 ,"Pitesti": {
                "Craiova": 138,
                "Rimnicu Vilcea": 97,
                "Bucharest": 101
                }
 ,"Bucharest": {
                "Pitesti": 101,
                "Fagaras": 211
                }
}



# def list_to_string(list_):
#     return '\n'.join(['-'.join(row) for row in list_])

# def string_to_list(string_):
#     return [row.split('-') for row in string_.split('\n')]


# def find_location(rows, element_to_find):
# 	print "Hellosdfddddddddddddddd"
# 	print rows
# 	for ir, row in enumerate(rows):
# 		for ic, element in enumerate(row):
# 			if element == element_to_find:
# 				return ir, ic


# # we create a cache for the goal position of each piece, so we don't have to
# # recalculate them every time
# goal_positions = {}
# rows_goal = string_to_list(GOAL)
# for number in '12345678e':
#     goal_positions[number] = find_location(rows_goal, number)

class EigthPuzzleProblem(SearchProblem):
    def actions(self, state):
        '''Returns a list of the pieces we can move to the empty space.'''
      #   actions=[]
      #   for key, value in graph[str(state)].iteritems():
    		# temp = [key,value]
    		# actions.append(temp)
        return graph[state].keys()

    def result(self, state, action):
        '''Return the resulting state after moving a piece to the empty space.
           (the "action" parameter contains the piece to move)
        '''
        # rows = string_to_list(state)
        # row_e, col_e = find_location(rows, 'e')
        # row_n, col_n = find_location(rows, action)

        # rows[row_e][col_e], rows[row_n][col_n] = rows[row_n][col_n], rows[row_e][col_e]
        

        # rows.append(graph[state][action])
        return action

    def is_goal(self, state):
        '''Returns true if a state is the goal state.'''
        return str(state) == str(GOAL)

    def cost(self, state1, action, state2):
        '''Uniform cost
        '''
        return int(graph[state1][action])

start = timer()
result = iterative_limited_depth_first(EigthPuzzleProblem(INITIAL), graph_search=True)
end = timer()

# Time
print "Time: " + str(end - start)

# cost of solution
print result.cost

# Solution
for action, state in result.path():
    print 'Move number', action
    print state
