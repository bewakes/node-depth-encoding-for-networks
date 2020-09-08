from typing import Tuple, Dict, NewType, List

Node = NewType('Node', int)
AdjacantNodes = NewType('AdjacantNodes', List[Node])
Tree = NewType('Tree', Dict[Node, AdjacantNodes])
NodeIndex = NewType('NodeIndex', Dict[Node, int])


def node_depth_encode(tree: Tree, root: Node) -> Tuple[NodeIndex, List[int]]:
    nodes = tree.keys()
    initial_node_index = {}
    root_index = 0
    root_depth = 0
    curr_index, depths, node_index = preorder(tree, root, [0]*len(nodes), initial_node_index, root_index, root_depth)
    return node_index, depths


def preorder(tree: Tree, node: Node, depths: List[int], node_index: NodeIndex, curr_index: int, curr_depth: int):
    """Calculate preorder of given tree"""
    node_index[node] = curr_index
    depths[curr_index] = curr_depth
    for adj_node in tree[node]:
        curr_index, depths, node_index = preorder(tree, adj_node, depths, node_index, curr_index+1, curr_depth+1)
    return curr_index, depths, node_index


"""
The following is a adjacancy list representation of T_from tree in figure 3 of the paper:
    Node-Depth Encoding and MultiobjectiveEvolutionary Algorithm Applied to Large-ScaleDistribution System Reconfiguration
"""

TREE: Tree = {
    1: [4],
    4: [5, 10],
    5: [6],
    10: [11, 16],
    6: [],
    11: [12],
    12: [],
    16: [22, 23],
    22: [],
    23: [],
}


if __name__ == '__main__':
    root: Node = 1
    print(node_depth_encode(TREE, root))
