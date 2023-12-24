class File2List:
    def __init__(self, path_to_file):
        self.list = []
        self.path_to_file = path_to_file
        self.create_list()

    def create_list(self):
        with open(self.path_to_file) as file:
            self.list = file.readlines()