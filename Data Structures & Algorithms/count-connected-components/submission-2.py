from collections import defaultdict
from typing import List



class Solution:
    def explore(self,graph,visited,current):
        if current in visited:
            return False
        visited.add(current)
        for nei in graph[current]:
            self.explore(graph,visited,nei)
        return True
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u,v in edges:

            graph[u].append(v)
            graph[v].append(u)

        visited= set()
        c=0
        for node in range(n):
            if node not in visited:
                self.explore(graph,visited,node)
                c+=1
        return c

