from typing import Tuple, Dict, NewType, List

Node = NewType('Node', int)
AdjacantNodes = NewType('AdjacantNodes', List[Node])
Tree = NewType('Tree', Dict[Node, AdjacantNodes])
NodeIndex = NewType('NodeIndex', Dict[Node, int])


def node_depth_encode(tree: Tree, root: Node) -> 'NodeDepthEncodedTree':
    root_depth = 0
    nodes, depths = preorder(tree, root, [], [], root_depth)
    return NodeDepthEncodedTree(nodes, depths)


def preorder(tree: Tree, node: Node, nodes: List[Node], depths: List[int], curr_depth: int):
    """Calculate preorder of given tree
    Return: Tuple of nodes in pre order, and the depths
    """
    for adj_node in tree[node]:
        nodes, depths = preorder(tree, adj_node, nodes, depths, curr_depth+1)
    return [node, *nodes], [curr_depth, *depths]


def operator1(tree_from, tree_to, p, a):
    """Returns (new_tree_from, new_tree_to).
    Does not modify original trees.
    AKA Preserve Ancestor Operator (PAO)
    """
    subtree_p = tree_from.get_subtree(p)
    return tree_from.prune_at(p), tree_to.insert_at(a, subtree_p)


def operator2(tree_from, tree_to, p, a, r):
    """Returns (new_tree_from, new_tree_to).
    Does not modify original trees
    AKA Change Ancestor Operator (CAO)
    """
    pass


class NodeDepthEncodedTree:
    def __init__(self, nodes, depths):
        self.nodes = nodes
        self.nodes_indices = {x: i for i, x in enumerate(nodes)}
        self.depths = depths

    def get_depth(self, node):
        node_index = self.nodes_indices.get(node)
        if node_index is None:
            return None
        return self.depths[node_index]

    def insert_at(self, node, subtree):
        """Insert subreee at node and return new inserted tree"""
        node_index = self.nodes_indices.get(node)
        ind = node_index + 1
        node_depth = self.get_depth(node)

        subtree_new_depths = [x + node_depth + 1 for x in subtree.depths]
        new_tree_to_nodes = self.nodes[:ind] + subtree.nodes + self.nodes[ind:]
        new_tree_to_depths = self.depths[:ind] + subtree_new_depths + self.depths[ind:]
        return NodeDepthEncodedTree(new_tree_to_nodes, new_tree_to_depths)

    def prune_at(self, node):
        start, end = self.get_subtree_indices_range(node)

        pruned_nodes = self.nodes[0: start] + self.nodes[end:]
        pruned_depths = self.depths[0: start] + self.depths[end:]
        return NodeDepthEncodedTree(pruned_nodes, pruned_depths)

    def get_subtree_indices_range(self, node):
        """Return array index range for subtree at node
        """
        node_index = self.nodes_indices.get(node)
        if node_index is None:
            return None
        node_depth = self.depths[node_index]

        # Create new set of nodes and depths
        node_index += 1
        while node_index < len(self.depths) and self.depths[node_index] > node_depth:
            node_index += 1
        return self.nodes_indices.get(node), node_index

    def get_subtree(self, node):
        node_index = self.nodes_indices.get(node)
        if node_index is None:
            return None
        node_depth = self.depths[node_index]

        start, end = self.get_subtree_indices_range(node)

        # Create new set of nodes and depths
        new_nodes = self.nodes[start: end]
        node_depth = self.depths[node_index]
        new_depths = [self.depths[x] - node_depth for x in range(start, end)]

        return NodeDepthEncodedTree(new_nodes, new_depths)

    def __eq__(self, othertree):
        return (
            self.depths == othertree.depths and
            self.nodes_indices == othertree.nodes_indices and
            self.nodes == othertree.nodes
       )

    def print(self):
        print("Depths : ", ' '.join([str(x).ljust(4) for x in self.depths]))
        print("Nodes  : ", ' '.join([str(x).ljust(4) for x in self.nodes]))


"""
The following is a adjacancy list representation of T_from tree in figure 3 of the paper:
    Node-Depth Encoding and MultiobjectiveEvolutionary Algorithm Applied to Large-ScaleDistribution System Reconfiguration
"""
TREE: Tree = {
    1: [4],
    4: [10, 5],
    5: [6],
    10: [16, 11],
    6: [],
    11: [12],
    12: [],
    16: [23, 22],
    22: [],
    23: [],
}


if __name__ == '__main__':
    root: Node = 1
    encoded_tree = node_depth_encode(TREE, root)
    encoded_tree.print()
    operator1(encoded_tree, None, 10, None)
