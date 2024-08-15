from typing import List, Set, Dict

from graphs.exceptions import NodeAlreadyExistsError, CycleInGraphError, NodeNotFoundError


class GNode:
    def __init__(self, name: str):
        self._name = name
        self._children = []

    def get_name(self) -> str:
        return self._name

    def get_children(self) -> List['GNode']:
        return self._children

    def add_child(self, child: 'GNode'):
        self._children.append(child)

    def __repr__(self):
        return self._name


class DAG:
    def __init__(self, root: GNode):
        """
        Initialize a Directed Acyclic Graph (DAG) with a root node.
        :param root: root node of the DAG.
        """
        self.root = root
        self.nodes: Dict[str, GNode] = {
            root.get_name(): root
        }

    def add_node(self, name: str) -> GNode:
        """
        Add a node to the graph.
        :param name: Name of the node to add.
        :return: GNode object that was added to the graph.
        """
        if name in self.nodes:
            raise NodeAlreadyExistsError(f"Node with name {name} already exists in the DAG.")
        new_node = GNode(name)
        self.nodes[name] = new_node
        return new_node

    def add_edge(self, from_node: str, to_node: str):
        """
        Add an edge from `from_node` to `to_node` in the graph.
        :param from_node: Source node name.
        :param to_node:  Target node name.
        """
        if from_node not in self.nodes or to_node not in self.nodes:
            raise NodeNotFoundError("Both nodes must exist in the DAG before adding an edge.")

        from_node_obj = self.nodes[from_node]
        to_node_obj = self.nodes[to_node]

        # Check for cycles
        if self._creates_cycle(from_node_obj, to_node_obj):
            raise CycleInGraphError("Adding this edge would create a cycle, which is not allowed in a DAG.")

        from_node_obj.add_child(to_node_obj)

    def _creates_cycle(self, from_node: GNode, to_node: GNode) -> bool:
        """Check if adding an edge from `from_node` to `to_node` would create a cycle.
        :param from_node: Node to add an edge from.
        :param to_node: Node to add an edge to.
        :return:
            Boolean indicating if adding the edge would create a cycle.
        """
        visited = set()
        return self._dfs_check_cycle(to_node, from_node.get_name(), visited)

    def _dfs_check_cycle(self, node: GNode, target_name: str, visited: Set[str]) -> bool:
        """
        Perform a depth-first search (DFS) traversal of the graph starting from `node` to check if there is a path to
        :param node: node to start the traversal from.
        :param target_name: target node name to check for a cycle.
        :param visited: Set of node names that have been visited during the traversal.
        :return:
            Boolean indicating if a cycle is detected.
        """
        if node.get_name() in visited:
            return False

        visited.add(node.get_name())

        if node.get_name() == target_name:
            return True

        for child in node.get_children():
            if self._dfs_check_cycle(child, target_name, visited):
                return True

        visited.remove(node.get_name())
        return False

    # This is the part of the coding task for 1a -----------------------------------------------------------------------
    def walk_graph(self) -> List[GNode]:
        """
        Perform a depth-first search (DFS) traversal of the graph starting from the root node.
        :return:
            List of GNodes in the order they were visited during the traversal.
        """

        def dfs(node: GNode, visited: Set[str], result: List[GNode]):
            if node.get_name() not in visited:
                visited.add(node.get_name())
                result.append(node)
                for child in node.get_children():
                    dfs(child, visited, result)

        visited = set()
        result = []
        dfs(self.root, visited, result)
        return result
    # -------------------------------------------------------------------------------------------------------------------

    # This is the part of the coding task for 1b -----------------------------------------------------------------------
    def paths(self) -> List[List[GNode]]:
        """
        Return all paths from the root node to leaf nodes in the graph.
        :return:
            List of GNodes, where each path is a list of nodes from the root to a leaf node.
        """
        def dfs_paths(node: GNode, current_path: List[GNode], all_paths: List[List[GNode]]):
            current_path.append(node)

            # If node has no children, it is a leaf node and a path is complete
            if not node.get_children():
                all_paths.append(current_path.copy())
            else:
                # If node has children, continue the DFS for each child
                for child in node.get_children():
                    dfs_paths(child, current_path, all_paths)

            # Backtrack to explore other paths
            current_path.pop()

        result = []
        dfs_paths(self.root, [], result)
        return result
    # ------------------------------------------------------------------------------------------------------------------

