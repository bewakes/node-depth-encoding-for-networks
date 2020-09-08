from nde import node_depth_encode, NodeDepthEncodedTree

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
    assert False


def test_operator2():
    assert False


def test():
    test_encoding()
    test_subtree()


test()
