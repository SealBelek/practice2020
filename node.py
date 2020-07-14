class Node:
    """
    create node for graph
    """
    def __init__(self, id, edges):
        """
        :param id: int
        :param edges: dict "id":"weight"
        """
        self.id = id
        self.edges = edges


def decode_json_to_nodes(dct):
    """
    object_hook for json.loads
    :return: Node
    """
    if "__complex__" in dct:
        return Node(dct["id"], dct["edges"])
    return dct
