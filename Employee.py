class Employee:
    name: str
    id: int

    def __init__(self, name, id):
        self.name = name
        self.__id = id
        print(f"Employee '{self.name}' is created.")

    def set_id(self, new_id):
        self.__id = new_id

    def get_id(self):
        return self.__id
