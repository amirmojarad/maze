class FileHandler:
    def __init__(self, file_name) -> None:
        super().__init__()
        self._file_name = file_name
        self._file = None

    def open_file(self):
        self._file = open(self._file_name, "r")

    def close_file(self):
        self._file.close()

    def read(self):
        return self._file.read()

