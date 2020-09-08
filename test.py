from nde import node_depth_encode, NodeDepthEncodedTree, operator1

"""
The following is a adjacancy list representation of T_from tree in figure 3 of the paper:
    Node-Depth Encoding and MultiobjectiveEvolutionary Algorithm Applied to Large-ScaleDistribution System Reconfiguration
"""
input_tree = {
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

input_root = 1


def test_encoding():
    expected_nodes_order = [1, 4, 5, 6, 10, 11, 12, 16, 22, 23]
    expected_node_depths = [0, 1, 2, 3, 2, 3, 4, 3, 4, 4]
    expected_endoced_tree = NodeDepthEncodedTree(expected_nodes_order, expected_node_depths)

    encoded_tree = node_depth_encode(input_tree, input_root)
    assert encoded_tree == expected_endoced_tree
    print('Test Encoding: PASS')


def test_subtree():
    encoded_tree = node_depth_encode(input_tree, input_root)
    p_node = 10
    expected_sub_nodes_order = [10, 11, 12, 16, 22, 23]
    expected_sub_nodes_depth = [0, 1, 2, 1, 2, 2]
    expected_subtree = NodeDepthEncodedTree(expected_sub_nodes_order, expected_sub_nodes_depth)
    assert expected_subtree == encoded_tree.get_subtree(p_node)
    print('Test Subtree: PASS')


def test_operator1():
    tree_from_nodes = [1, 4, 5, 6, 10, 11, 12, 16, 22, 23]
    tree_from_depths = [0, 1, 2, 3, 2, 3, 4, 3, 4, 4]
    tree_from = NodeDepthEncodedTree(tree_from_nodes, tree_from_depths)

    tree_to_nodes = [3, 27, 21, 20, 26, 19, 18, 17, 25, 24]
    tree_to_depths = [0, 1, 2, 3, 2, 3, 4, 5, 3, 4]
    tree_to = NodeDepthEncodedTree(tree_to_nodes, tree_to_depths)

    p = 11
    a = 17

    new_tree_from_nodes = [1, 4, 5, 6, 10, 16, 22, 23]
    new_tree_from_depths = [0, 1, 2, 3, 2, 3, 4, 4]
    new_tree_from = NodeDepthEncodedTree(new_tree_from_nodes, new_tree_from_depths)

    new_tree_to_nodes = [3, 27, 21, 20, 26, 19, 18, 17, 11, 12, 25, 24]
    new_tree_to_depths = [0, 1, 2, 3, 2, 3, 4, 5, 6, 7, 3, 4]
    new_tree_to = NodeDepthEncodedTree(new_tree_to_nodes, new_tree_to_depths)

    expected_new_tree_from, expected_new_tree_to = operator1(tree_from, tree_to, p, a)
    assert new_tree_from == expected_new_tree_from
    assert new_tree_to == expected_new_tree_to
    print('TEST OPERATOR 1: PASS')


def test_operator2():
    assert False
    print('TEST OPERATOR 2: PASS')


def test():
    test_encoding()
    test_subtree()
    test_operator1()
    test_operator2()


test()
