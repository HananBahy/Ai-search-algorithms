#!/usr/bin/python
#
### Student Info
# Smith, Christopher, 02386569, 159.302
# Assignment 1: 8 Puzzle.
#
### Language
# This assignment was written in Python. An open source, interpreted language
# with a mix of imperative, OO and functional programming. Syntax is simple
# and easy to learn.
#
# Developed on Ubuntu Linux but this will run on the interpreter available
# from http://python.org. Documentation is also on that site but a good
# tutorial is available for free at http://diveintopython.org.
#
### Data Structures
#
# The state of the board is stored in a list. The list stores values for the
# board in the following positions:
#
# -------------
# | 0 | 3 | 6 |
# -------------
# | 1 | 4 | 7 |
# -------------
# | 2 | 5 | 8 |
# -------------
#
# The goal is defined as:
#
# -------------
# | 1 | 2 | 3 |
# -------------
# | 8 | 0 | 4 |
# -------------
# | 7 | 6 | 5 |
# -------------
#
# Where 0 denotes the blank tile or space.
goal_state = [1, 8, 7, 2, 0, 6, 3, 4, 5]

#state=[1, 8, 7, 2, 3, 6, 0, 5,4]


#
# The code will read state from a file called "state.txt" where the format is
# as above but space seperated. i.e. the content for the goal state would be
# 1 8 7 2 0 6 3 4 5

### Code begins.
import sys


def display_board(state):
    print( "-------------")
    print( "| %i | %i | %i |" % (state[0], state[3], state[6]))
    print( "-------------")
    print( "| %i | %i | %i |" % (state[1], state[4], state[7]))
    print( "-------------")
    print( "| %i | %i | %i |" % (state[2], state[5], state[8]))
    print( "-------------")


def move_up(state):
    """Moves the blank tile up on the board. Returns a new state as a list."""
    # Perform an object copy
    new_state = state[:]
    index = new_state.index(0)
    # Sanity check
    if index not in [0, 3, 6]:
        # Swap the values.
        temp = new_state[index - 1]
        new_state[index - 1] = new_state[index]
        new_state[index] = temp
        return new_state
    else:
        # Can't move, return None (Pythons NULL)
        return None


def move_down(state):
    """Moves the blank tile down on the board. Returns a new state as a list."""
    # Perform object copy
    new_state = state[:]
    index = new_state.index(0)
    # Sanity check
    if index not in [2, 5, 8]:
        # Swap the values.
        temp = new_state[index + 1]
        new_state[index + 1] = new_state[index]
        new_state[index] = temp
        return new_state
    else:
        # Can't move, return None.
        return None


def move_left(state):
    """Moves the blank tile left on the board. Returns a new state as a list."""
    new_state = state[:]
    index = new_state.index(0)
    # Sanity check
    if index not in [0, 1, 2]:
        # Swap the values.
        temp = new_state[index - 3]
        new_state[index - 3] = new_state[index]
        new_state[index] = temp
        return new_state
    else:
        # Can't move it, return None
        return None


def move_right(state):
    """Moves the blank tile right on the board. Returns a new state as a list."""
    # Performs an object copy. Python passes by reference.
    new_state = state[:]
    index = new_state.index(0)
    # Sanity check
    if index not in [6, 7, 8]:
        # Swap the values.
        temp = new_state[index + 3]
        new_state[index + 3] = new_state[index]
        new_state[index] = temp
        return new_state
    else:
        # Can't move, return None
        return None


def create_node(state, parent, operator, depth, cost):
    return Node(state, parent, operator, depth, cost)


def expand_node(node):
    """Returns a list of expanded nodes"""
    expanded_nodes = []
    expanded_nodes.append(create_node(move_up(node.state), node, "u", node.depth + 1, 0))
    expanded_nodes.append(create_node(move_down(node.state), node, "d", node.depth + 1, 0))
    expanded_nodes.append(create_node(move_left(node.state), node, "l", node.depth + 1, 0))
    expanded_nodes.append(create_node(move_right(node.state), node, "r", node.depth + 1, 0))
    # Filter the list and remove the nodes that are impossible (move function returned None)
    expanded_nodes = [node for node in expanded_nodes if node.state != None]  # list comprehension!
    return expanded_nodes


def bfs(start, goal):
    """Performs a breadth first search from the start state to the goal"""
    # A list (can act as a queue) for the nodes.'
    fringe=[]
    fringe.append(create_node(start, None, None, 1, 0))
    while(True):
        current=fringe.pop(0) #fringe acts like queue

        if current.state == goal:
            CNode=current
           # print(CNode.parent)        
            operators=[]
            while CNode.depth !=1:
                #print(CNode.depth)
                operators.insert(0,CNode.operator)
                CNode=CNode.parent
                
            return operators
                
                
        #print("NO")    
        fringe.extend(expand_node(current))  #in case of "else"
        
        

"""def ucs(start, goal):
    ###Performs an uniformed cost search from the start state to the goal##
    # A list (can act as a queue) for the nodes.'
    fringe=[]       #priority queue
    fringe.append(create_node(start, None, None, 1, 0))
    current=fringe.pop()
    while(True):
        #current=fringe.pop(0) #fringe acts like queue

        if current.state == goal:
            CNode=current
            print("cost = ",current.cost)
           # print(CNode.parent) 
            operators=cost(current)     #current becomes goal          
            return operators
                              
        else:
            if fringe==[]:   #in case of first iteration
                expanded=expand_node(current)   #list of nodes
                for item in expanded:
                    #item.cost+=1   #false way
                    cost(item)
                    fringe.append(item)
            min_cost=fringe[0].cost
            min_index=0
            for i in range(1,len(fringe)):
                if fringe[i].cost<min_cost:
                    min_cost=fringe[i].cost
                    min_index=i
            current=fringe.pop(min_index)
            #print("cost",current.cost)
            #fringe.extend(expand_node(current))
            expanded=expand_node(current)   #list of nodes
            for item in expanded:
                    #item.cost+=1   #false way
                    cost(item)
                    fringe.append(item)"""
                    
#use depth to find cost,it is simple way
def ucs(start, goal):
    """Performs an uniformed cost search from the start state to the goal"""
    # A list (can act as a queue) for the nodes.'
    fringe=[]       #priority queue
    fringe.append(create_node(start, None, None, 1, 0))
    current=fringe.pop()
    while(True):
        if current.state == goal:
            print("cost = ",current.cost) 
            operators=cost(current)     #current becomes goal          
            return operators
                              
        else:
            if fringe==[]:   #in case of first iteration
                expanded=expand_node(current)   #list of nodes
                for item in expanded:
                    #cost(item)  
                    item.cost+=item.parent.depth
                    fringe.append(item)
            min_cost=fringe[0].cost
            min_index=0
            for i in range(1,len(fringe)):
                if fringe[i].cost<min_cost:
                    min_cost=fringe[i].cost
                    min_index=i
            current=fringe.pop(min_index)
             #expand
            expanded=expand_node(current)   #list of nodes
            for item in expanded:
                    #cost(item)
                    item.cost+=item.parent.depth
                    fringe.append(item)
        
def greedy(start, goal):
    """Performs a greedy search from the start state to the goal"""
    # A list (can act as a queue) for the nodes.'
    fringe=[]       #priority queue   #each element is list of 2 elements ( node and its heuristic)
    first_node=create_node(start, None, None, 1, 0)
    fringe.append([first_node,h(first_node.state, goal)])
    current=fringe.pop()
    while(True):
        if current[0].state == goal:
            print("heuristic =",current[1])
            operators=[]
            operators=cost(current[0])
            return operators
                
                
        else:
            if fringe==[]:   #in case of first iteration
                expanded=expand_node(current[0])   #list of nodes
                for item in expanded:
                    fringe.append([item,h(item.state, goal)])
            #in case of false
            min_h=fringe[0][1]
            min_index=0
            for i in range(1,len(fringe)):
                if fringe[i][1]<min_h:
                    min_h=fringe[i][1]
                    min_index=i
            current=fringe.pop(min_index)
            #expand
            expanded=expand_node(current[0])   #list of nodes
            for item in expanded:
                    fringe.append([item,h(item.state, goal)])
            #fringe.extend(expand_node(current))
            
def a_star(start, goal):  #expand node that has minimum f in fringe
    """Perfoms an A* heuristic search"""
    fringe=[]       #priority queue   #each element is list of 2 elements ( node and its f(n))
    first_node=create_node(start, None, None, 1, 0)
    fringe.append([first_node,f(first_node, goal)])
    current=fringe.pop()
    while(True):
        if current[0].state == goal:
            print("f =",current[1])   #in this case f=cost as h=0 (because current[1] is the same goal)
           # print(CNode.parent)        
            operators=cost(current[0])                    
            return operators
                                
        else:
            if fringe==[]:   #in case of first iteration
                expanded=expand_node(current[0])   #list of nodes
                for item in expanded:
                    fringe.append([item,f(item, goal)])
            #in case of false
            min_f=fringe[0][1]
            min_index=0
            for i in range(1,len(fringe)):
                if fringe[i][1]<min_f:
                    min_f=fringe[i][1]
                    min_index=i
            current=fringe.pop(min_index)
            #expand
            expanded=expand_node(current[0])   #list of nodes
            for item in expanded:
                    fringe.append([item,f(item, goal)])
            #fringe.extend(expand_node(current))


def dfs(start, goal, depth=10):
    """Performs a depth first search from the start state to the goal. Depth param is optional."""
    # NOTE: This is a limited search or else it keeps repeating moves. This is an infinite search space.
    # I'm not sure if I implemented this right, but I implemented an iterative depth search below
    # too that uses this function and it works fine. Using this function itself will repeat moves until
    # the depth_limit is reached. Iterative depth search solves this problem, though.
    #
    # An attempt of cutting down on repeat moves was made in the expand_node() function.
    
    fringe=[]
    fringe.append(create_node(start, None, None, 1, 0))
    while(True):
        current=fringe.pop() #fringe acts like stack

        if current.state == goal:
            CNode=current
           # print(CNode.parent)        
            operators=[]
            while CNode.depth !=1:
                #print(CNode.depth)
                operators.insert(0,CNode.operator)
                CNode=CNode.parent
                
            return operators
                
                
        else:
            if current.depth<depth:
                fringe.extend(expand_node(current))  
        


def cost(current):   #assign the cost of current node
    operators=[]
    CNode=current
    while CNode.depth !=1:
        #print(CNode.depth)
        operators.insert(0,CNode.operator)
        CNode=CNode.parent
    current.cost=len(operators)
    return operators #use return value in case of I need it
########
def f(current,goal):
    heur=h(current.state, goal)   #huristic
    if current.depth!=1:
        current.cost += current.parent.depth
    f_n=heur + current.cost
    return  f_n   #f(n) = g(n) + h(n)
    
    
###############
def h(state, goal):
    """Heuristic for the A* search. Returns an integer based on out of place tiles"""
    heuristic=0    #initial value   #number of numbers aren't in its place
    for i in range(len(state)):
        
        if state[i]!=goal[i]:
            heuristic+=1
    return heuristic
########

# Node data structure
class Node:
    def __init__(self, state, parent, operator, depth, cost):
        # Contains the state of the node
        self.state = state
        # Contains the node that generated this node
        self.parent = parent
        # Contains the operation that generated this node from the parent
        self.operator = operator
        # Contains the depth of this node (parent.depth +1)
        self.depth = depth
        # Contains the path cost of this node from depth 0. Not used for depth/breadth first.
        self.cost = cost


def readfile(filename):
    f = open(filename)
    data = f.read()
    # Get rid of the newlines
    data = data.strip("\n")
    # Break the string into a list using a space as a seperator.
    data = data.split(" ")
    state = []
    for element in data:
        state.append(int(element))
    return state


# Main method
def main():
    starting_state = readfile("state.txt")
    ### CHANGE THIS FUNCTION TO USE bfs, dfs, ids or a_star
    result = bfs(starting_state, goal_state)
    #result = ucs(starting_state, goal_state)
    #result = greedy(starting_state, goal_state)
    #result = a_star(starting_state, goal_state)
    #result = dfs(starting_state, goal_state)
    
    if result == None:
        print( "No solution found")
    elif result == [None]:
        print( "Start node was the goal!")
    else:
        print( result)
        print( len(result), " moves")
        #print(h(state, goal_state))


# A python-isim. Basically if the file is being run execute the main() function.
if __name__ == "__main__":
    main()