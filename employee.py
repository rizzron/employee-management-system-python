class Employee:
    name: str
    id: int

    def __init__(self, name, id):
        self.name = name
        self.__id = id

