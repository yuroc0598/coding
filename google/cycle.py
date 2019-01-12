#!/usr/bin/python3


# detect cycle in undirected graph: disjoint set union

# detect cycle in directed graph: dfs


def cycleDirected(G):
    def helper(node,checked,checking):
        if node not in G:
            return False
        if node in checked:
            return True
        if node in checking:
            return False
        checked.add(node)
        for k in G[node]:
           if helper(k,checked,checking):
                return True
        return False
    visited = set()
    for node in G:
        if node not in visited:
            checking = set()
            if helper(node,visited,checking):
                return True
    return False


G1={0:[1,2],1:[2],2:[0,3],3:[3]}
G2={0:[1],1:[0]}
print(cycleDirected(G1))
checked = set()
print(cycleDirected(G2))
