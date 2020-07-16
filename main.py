import json

import node

with open("data/nodes.json") as json_file:
    json_file = json_file.read()
    nodes = json.loads(json_file, object_hook=node.decode_json_to_nodes)

nodes = {node.id:node.edges for node in nodes}