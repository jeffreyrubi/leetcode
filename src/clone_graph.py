# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from typing import Optional
class Solution:
    def createNode(self, node, registry):
        if node is None or node.val in registry:
            return
        else:
            registry[node.val] = Node(node.val)

        for neighbor in node.neighbors:
            self.createNode(neighbor, registry)
            registry[node.val].neighbors.append(registry[neighbor.val])

            
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        registry = {}
        
        if node is None:
            return None

        self.createNode(node, registry) 
        return registry[node.val]


