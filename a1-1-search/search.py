# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    # from game import Directions
    # s = Directions.SOUTH
    # w = Directions.WEST
    # n = Directions.NORTH
    # e = Directions.EAST

    #start node
    startingNode = problem.getStartState()
    print(startingNode)
    if problem.isGoalState(startingNode): #start is goal
        return []
    #import stack
    stack = util.Stack()
    #visited node
    visited = []
    #push start node to stack
    stack.push((startingNode,[]))
    
    #loop stack not empty and goal not reach
    while stack.isEmpty() != True :
        #check the most recently push
        currentState, CurrMove = stack.pop()
        if currentState not in visited:
            #if this node not visited the mark it visited
            visited.append(currentState)
            #if this node is goal
            if problem.isGoalState(currentState):
                return CurrMove
            else:
                #list all possible successor node
                for i in problem.getSuccessors(currentState):
                    if i not in visited:
                        stack.push((i[0], CurrMove + [i[1]]))
    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    #start node
    startingNode = problem.getStartState()
    print(startingNode)
    if problem.isGoalState(startingNode): #start is goal
        return []
    #import queue
    queue = util.Queue()
    #visited node
    visited = []
    queue.push((startingNode, []))

    #loop
    while queue.isEmpty() != True:
        currState, currMove = queue.pop()
        if currState not in visited:
            visited.append(currState)
            if problem.isGoalState(currState):
                return currMove
            else:
                for i in problem.getSuccessors(currState):
                    if i not in visited:
                        queue.push((i[0], currMove + [i[1]]))
    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    #start node
    startingNode = (problem.getStartState(), [], 0)
    print(startingNode)
    if problem.isGoalState(startingNode): #start is goal
        return []
    #import queue
    queue = util.PriorityQueue()
    #visited node
    visited = {}
    queue.push(startingNode, 0)

    #loop
    while queue.isEmpty() != True:
        currState, currMove, currCost = queue.pop()
        if currState not in visited or currCost < visited[currState]: 
            visited[currState] = currCost
            if problem.isGoalState(currState):
                return currMove
            else:
                for i in problem.getSuccessors(currState):
                    if i not in visited:
                        bestAction = currMove + [i[1]]
                        bestCost = currCost + i[2]
                        BestNode = (i[0], bestAction, bestCost)
                        # queue.push(BestNode, bestCost)
                        queue.update(BestNode, bestCost)

    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"

    #start node 
    startingNode = (problem.getStartState(), [], 0)
    print(startingNode)
    if problem.isGoalState(startingNode): #start is goal
        return []
    #import queue
    queue = util.PriorityQueue()
    #visited node
    visited = {}
    queue.push(startingNode, 0)

    #loop
    while queue.isEmpty() != True:
        currState, currMove, currCost = queue.pop()
        if currState not in visited or currCost < visited[currState]: 
            visited[currState] = currCost
            if problem.isGoalState(currState):
                return currMove
            else:
                for i in problem.getSuccessors(currState):
                    if i not in visited:
                        Action = currMove + [i[1]]
                        Cost = currCost + i[2]
                        totalCost = Cost + heuristic(i[0], problem)
                        BestNode = (i[0], Action, Cost)
                        # queue.push(BestNode, totalCost) #Test
                        queue.update(BestNode, totalCost)

    util.raiseNotDefined()


#####################################################
# EXTENSIONS TO BASE PROJECT
#####################################################

# Extension Q1e
def iterativeDeepeningSearch(problem):
    """Search the deepest node in an iterative manner."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


#####################################################
# Abbreviations
#####################################################
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
ids = iterativeDeepeningSearch
