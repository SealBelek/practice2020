from datetime import datetime

import service
import start_gui
import mapGrapth

if __name__ == '__main__':
    graph = mapGrapth.MapGraph(1)
    graph.add_service(service.Service('milk', [4, 1, 2], datetime.strptime("00:00:00", '%H:%M:%S')))
    graph.add_service(service.Service('repair', [3, 2, 1, 4], datetime.strptime("00:00:00", '%H:%M:%S')))
    graph.add_service(service.Service('smth', [5, 6, 4], datetime.strptime("00:00:00", '%H:%M:%S')))
    start_gui.gui("\n".join(graph.create_time_table()))
