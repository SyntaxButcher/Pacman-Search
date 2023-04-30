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
import time

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
    
    #Finding the initial state
    InitialState = problem.getStartState()
    #Initializing the first node, frontier, explored set
    InitialNode = (InitialState, [])
    Frontier = [InitialNode]
    ExploredSet = []
    while len(Frontier) != 0:
        #Popping last element from Frontier and adding to current node
        CurrentNode = Frontier.pop()
        nodePath = CurrentNode[1]
        #Adding current node to explored set or brekaing out if end goal
        if CurrentNode[0] not in ExploredSet:
            ExploredSet.append(CurrentNode[0])
        if problem.isGoalState(CurrentNode[0]):
            break
        #All the possible successor nodes -> checking in exploredSet and current frontier before adding to frontier
        PossibleSuccessors = problem.getSuccessors(CurrentNode[0])
        #Extracting the coordinates and directions from the possible successors output
        for i in PossibleSuccessors:
            if i[0] not in ExploredSet:
                a = i[1]
                Frontier.append((i[0], nodePath + [a]))
    return nodePath
    util.raiseNotDefined()


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""

    #Finding the initial state
    InitialState = problem.getStartState()
    #Initializing the first node, frontier, explored set and frontier coord set
    InitialNode = (InitialState, [])
    Frontier = [InitialNode]
    ExploredSet = []
    while len(Frontier) != 0:
        #Popping first element from Frontier and adding to current node
        CurrentNode = Frontier.pop(0)
        nodePath = CurrentNode[1]
        #Extracting all the coordinates from frontier
        FrontierCoords = []
        for i in Frontier:
            FrontierCoords.append(i[0])
        #Adding current node to explored set or brekaing out if end goal
        if CurrentNode[0] not in ExploredSet:
            ExploredSet.append(CurrentNode[0])
        if problem.isGoalState(CurrentNode[0]):
            break
        #All the possible successor nodes -> checking in exploredSet and current frontier before adding to frontier
        PossibleSuccessors = problem.getSuccessors(CurrentNode[0])
        #Extracting the coordinates and directions from the possible successors output
        for i in PossibleSuccessors:
            if i[0] not in ExploredSet and i[0] not in FrontierCoords:
                a = i[1]
                Frontier.append((i[0], nodePath + [a]))
    return nodePath
    
    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    
    #Finding the initial state
    InitialState = problem.getStartState()
    if problem.isGoalState(InitialState):
            return []
    #Initializing the first node, frontier, explored set
    InitialNode = (InitialState, [], 0)
    Frontier = [InitialNode]
    ExploredSet = []  
    while len(Frontier) != 0:
        #selecting lowest cost frontier as current node
        lowest = 999999999999999999999
        for i in Frontier:
            if i[2] < lowest:
                lowest = i[2]
        for i in Frontier:
            if i[2] == lowest:
                CurrentNode = i
        #removing node from frontier
        Frontier.remove(CurrentNode)
        FrontierCoords = []
        for i in Frontier:
            FrontierCoords.append(i[0])
        #extracting node coords, direction, cost and frontier coord
        CurrentCoord = CurrentNode[0]
        CurrentPath = CurrentNode[1]
        CurrentCost = CurrentNode[2]
        #adding current node to explored set or breaking out if goal
        if CurrentCoord not in ExploredSet:
            ExploredSet.append(CurrentCoord)
        if problem.isGoalState(CurrentCoord):
            break
        #all the possible successor nodes checked and added to frontier
        PS = problem.getSuccessors(CurrentCoord)
        #extracting the coord and dir and cost 
        for i in PS:
            if i[0] not in ExploredSet and i[0] not in FrontierCoords:
                a = i[1]
                c = i[2]
                Frontier.append((i[0], CurrentPath + [a], CurrentCost + c))
            elif i[0] not in ExploredSet:
                a = i[0]
                b = CurrentPath + [i[1]]
                c = i[2] + CurrentCost
                for j in Frontier:
                    if j[0] == a:
                        if c < j[2]:
                            Frontier.remove(j)
                            Frontier.append((a,b,c))
    return CurrentPath

    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    
    #Finding the initial state
    InitialState = problem.getStartState()
    #Initializing the first node, frontier, explored set, Heuristic and frontier coord set
    InitialHeuristic = heuristic(InitialState,problem)
    InitialNode = (InitialState, [], InitialHeuristic, 0)
    Frontier = [InitialNode]
    ExploredSet = []
    while len(Frontier) != 0:
        #selecting lowest heuristic+cost as current node
        lowest = 99999999999999999999999
        for i in Frontier:
            if i[2] < lowest:
                lowest = i[2]
        for i in Frontier:
            if i[2] == lowest:
                CurrentNode = i
        #removing node from frontier
        Frontier.remove(CurrentNode)
        FrontierCoords = []
        for i in Frontier:
            FrontierCoords.append(i[0])
        #extracting node coords, direction, Astar_cost, cost and frontier coord
        CurrentCoord = CurrentNode[0]
        CurrentPath = CurrentNode[1]
        CurrentAstar = CurrentNode[2]
        CurrentCost = CurrentNode[3]
        #adding current node to explored set or brekaing out if goal
        if CurrentCoord not in ExploredSet:
            ExploredSet.append(CurrentCoord)
        if problem.isGoalState(CurrentCoord):
            break
        #all the possible successor nodes checked and added to frontier & extracting coord,dir and Astar cost
        PS = problem.getSuccessors(CurrentCoord)
        for i in PS:
            if i[0] not in ExploredSet and i[0] not in FrontierCoords:
                a = i[1]
                #adding heuristic to cost
                c = i[2] + CurrentCost + heuristic(i[0],problem) 
                Frontier.append((i[0], CurrentPath + [a], c, CurrentCost + i[2]))
            elif i[0] not in ExploredSet:
                a = i[0]
                b = CurrentPath + [i[1]]
                c = i[2] + CurrentCost + heuristic(i[0],problem)
                d = CurrentCost + i[2]
                for j in Frontier:
                    if j[0] == a:
                        if c < j[2]:
                            Frontier.remove(j)
                            Frontier.append((a,b,c,d))
    return CurrentPath

    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
