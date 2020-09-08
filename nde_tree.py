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
        node_depth = self.get_depth(node)
        # By default the placement of subtree is next to the node index
        insert_index = node_index + 1
        # But, in case node already has child, we don't want to break the index order
        # So we calculate the next position where we can insert the subtree which is the
        # next index where depth is less than or equal to node depth
        length = len(self.nodes)
        while insert_index < length and self.depths[insert_index] > node_depth:
            insert_index += 1

        subtree_new_depths = [x + node_depth + 1 for x in subtree.depths]
        new_tree_to_nodes = self.nodes[:insert_index] + subtree.nodes + self.nodes[insert_index:]
        new_tree_to_depths = self.depths[:insert_index] + subtree_new_depths + self.depths[insert_index:]
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
            isinstance(othertree, NodeDepthEncodedTree) and
            self.depths == othertree.depths and
            self.nodes_indices == othertree.nodes_indices and
            self.nodes == othertree.nodes
        )

    def print(self, title=""):
        print(title)
        print("Depths : ", ' '.join([str(x).ljust(4) for x in self.depths]))
        print("Nodes  : ", ' '.join([str(x).ljust(4) for x in self.nodes]))
