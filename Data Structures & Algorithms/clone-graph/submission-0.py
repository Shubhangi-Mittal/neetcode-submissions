"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if not node:
            return None

        start=node
        stk=[start]
        visited=set()
        visited.add(start)
        o_to_n={}

        while stk:
            node=stk.pop() #we take old node
            o_to_n[node]=Node(val=node.val) #we create a new node map old and new node values

            for neigh in node.neighbors:
                if neigh not in visited:
                    visited.add(neigh) #take the old node see its neighbors if the neighbors arent visited add them to the set visited and to the stack
                    stk.append(neigh)

        for old_node, new_node in o_to_n.items():
            for n in old_node.neighbors: #each neighbor of the old node mapped as neighbor of the new node
                new_n=o_to_n[n] #mapped new node neighbors as the old node
                new_node.neighbors.append(new_n) #append to the list of new node neighbors

        return o_to_n[start]
        