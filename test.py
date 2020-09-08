from nde import node_depth_encode

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

expected_node_indices = {
    1: 0,
    4: 1,
    5: 2,
    6: 3,
    10: 4,
    11: 5,
    12: 6,
    16: 7,
    22: 8,
    23: 9
}

expected_node_depths = [0, 1, 2, 3, 2, 3, 4, 3, 4, 4]


def test():
    node_indices, node_depths = node_depth_encode(input_tree, input_root)
    assert node_indices == expected_node_indices
    assert node_depths == expected_node_depths
    print('PASS')


if __name__ == '__main__':
    test()
