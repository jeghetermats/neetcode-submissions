"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return Node(1).next
        original_nodes = []
        curr = head
        new_nodes = []
        
        while curr:
            original_nodes.append(curr)
            new_node = Node(curr.val)
            curr = curr.next
        
            new_nodes.append(new_node)
            
        index_of = {node: i for i, node in enumerate(original_nodes)}

        for i in range(len(original_nodes)):
            old_node = original_nodes[i]

            if i>0:
                new_nodes[i-1].next = new_nodes[i]

            if old_node.random:
                index_random = index_of[old_node.random]
                new_nodes[i].random = new_nodes[index_random]

        return new_nodes[0]