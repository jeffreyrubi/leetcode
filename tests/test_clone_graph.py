from src.clone_graph import Solution, Node

def test_clone_graph():
    solution = Solution()

    def build_graph(adj_list):
        if not adj_list:
            return None
        nodes = [Node(i+1) for i in range(len(adj_list))]
        for idx, neighbors in enumerate(adj_list):
            nodes[idx].neighbors = [nodes[n-1] for n in neighbors]
        return nodes[0]

    def compare_graphs(node1, node2):
        visited1, visited2 = set(), set()
        def dfs(n1, n2):
            if not n1 and not n2:
                return True
            if not n1 or not n2 or n1.val != n2.val:
                return False
            if n1 in visited1 or n2 in visited2:
                return True
            visited1.add(n1)
            visited2.add(n2)
            if len(n1.neighbors) != len(n2.neighbors):
                return False
            for neigh1, neigh2 in zip(n1.neighbors, n2.neighbors):
                if not dfs(neigh1, neigh2):
                    return False
            return True
        return dfs(node1, node2)

    # Test case 1: Example graph [[2,4],[1,3],[2,4],[1,3]]
    graph1 = build_graph([[2,4],[1,3],[2,4],[1,3]])
    cloned1 = solution.cloneGraph(graph1)
    assert compare_graphs(graph1, cloned1)

    # Test case 2: Single node graph [[]]
    graph2 = build_graph([[]])
    cloned2 = solution.cloneGraph(graph2)
    assert compare_graphs(graph2, cloned2)

    # Test case 3: Empty graph []
    graph2 = build_graph([])
    cloned2 = solution.cloneGraph(graph2)
    assert compare_graphs(graph2, cloned2)