import json
import datetime

import node


class MapGraph:
    def __init__(self, location):
        """
        :param location: int
        :return: MapGraph
        """
        with open("data/nodes.json") as json_file:
            json_file = json_file.read()
            self.nodes = json.loads(json_file, object_hook=self._decode_json_to_nodes)
        self.nodes = {node.id: node for node in self.nodes}
        self.location_id = location
        self.services = []

    def add_service(self, service):
        """

        :param service: Serivce
        """
        self.services.append(service)

    def create_time_table(self):
        time_table = []
        for srv in self.services:
            if self.location_id in srv.get_path():
                time_arrive = srv.get_time() + self._count_up_weights(srv.get_path())
                time_table.append(srv.get_name() + " " + str(time_arrive.time()))
        return time_table


    def _count_up_weights(self, path):
        len_path = datetime.timedelta(hours = 0)
        for i in range(len(path) - 1):
            if path[i] == self.location_id:
                break
            len_path = len_path + self.nodes[path[i]].get_edge_weight_from_id(path[i+1])
        return len_path

    def _decode_json_to_nodes(self, dct):
        """
        object_hook for json.loads
        :return: Node
        """
        if "__complex__" in dct:
            return node.Node(dct["id"], dct["edges"])
        return dct
