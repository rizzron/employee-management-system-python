class Employee:
    _id_counter = 1

    def __init__(self, name: str):
        self.name = name
        self.id = Employee._id_counter
        Employee._id_counter += 1

    def get_id(self) -> int:
        return self.id

