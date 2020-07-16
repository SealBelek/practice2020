import json

import node


def count_up_weight(path, nodes):
    sum_weight = 0
    for i in range(len(path) - 1):
        sum_weight += nodes[path[i]][path[i+1]]
    return sum_weight


with open("data/nodes.json") as json_file:
    json_file = json_file.read()
    nodes = json.loads(json_file, object_hook=node.decode_json_to_nodes)

nodes = {node.id:node.edges for node in nodes}
print(nodes[1][4])

print(count_up_weight([3, 4, 6], nodes))
