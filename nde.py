from typing import Tuple, Dict, NewType, List
from nde_tree import NodeDepthEncodedTree

Node = NewType('Node', int)
AdjacantNodes = NewType('AdjacantNodes', List[Node])
Tree = NewType('Tree', Dict[Node, AdjacantNodes])
NodeIndex = NewType('NodeIndex', Dict[Node, int])


def node_depth_encode(tree: Tree, root: Node) -> NodeDepthEncodedTree:
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


def operator1(tree_from: NodeDepthEncodedTree, tree_to: NodeDepthEncodedTree, p: Node, a: Node):
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
