class Node:
    """
    create node for graph
    """
    def __init__(self, id, edges):
        """
        :param id: int
        :param edges: dict "id":"weight"
        """
        new_edges = {} # str key to int key
        for key, value in edges.items():
            new_edges[int(key)] = value
            
        self.id = id
        self.edges = new_edges

    def get_edges_weight_from_id(self, id_node):
        return self.edges[id_node]

def decode_json_to_nodes(dct):
    """
    object_hook for json.loads
    :return: Node
    """
    if "__complex__" in dct:
        return Node(dct["id"], dct["edges"])
    return dct
