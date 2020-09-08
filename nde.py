from typing import Tuple, Dict, NewType, List

Node = NewType('Node', int)
AdjacantNodes = NewType('AdjacantNodes', List[Node])
Tree = NewType('Tree', Dict[Node, AdjacantNodes])
NodeIndex = NewType('NodeIndex', Dict[Node, int])


def node_depth_encode(tree: Tree, root: Node) -> Tuple[NodeIndex, List[int]]:
    nodes = tree.keys()
    root_depth = 0
    nodes, depths = preorder(tree, root, [], [], root_depth)
    return {x: i for i, x in enumerate(nodes)}, depths


def preorder(tree: Tree, node: Node, nodes: List[Node], depths: List[int], curr_depth: int):
    """Calculate preorder of given tree
    Return: Tuple of nodes in pre order, and the depths
    """
    for adj_node in tree[node]:
        nodes, depths = preorder(tree, adj_node, nodes, depths, curr_depth+1)
    return [node, *nodes], [curr_depth, *depths]


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
    print(node_depth_encode(TREE, root))
