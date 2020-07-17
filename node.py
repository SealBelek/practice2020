import datetime


class Node:
    """
    create node for graph
    """
    def __init__(self, id, edges):
        """
        :param id: int
        :param edges: dict "id":time
        """
        new_edges = {} # str key to int key
        for key, value in edges.items():
            new_edges[int(key)] = datetime.timedelta(hours=value)
            
        self.id = id
        self.edges = new_edges

    def get_edge_weight_from_id(self, id_node):
        """

        :param id_node: int
        :return: weight: time
        """
        return self.edges[id_node]
