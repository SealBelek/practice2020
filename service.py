class Service:
    def __init__(self, name_service, path_service, time):
        """

        :param name_service: string
        :param path_service: list(int)
        :param time: time
        """
        self.name = name_service
        self.path = path_service
        self.time = time

    def get_name(self):
        return self.name

    def get_path(self):
        return self.path

    def get_time(self):
        return self.time



