class Persona:
    def __init__(self, database_name):
        self.name = database_name

        self.data = {}
        self.id_counter = 0

    def create(self, data):
        """
        This method add a register in database and returns the associated ID
        Parameters
        ----------
        data: dict
            Data asociated to an student.
        Returns
        -------
        out: int
            ID of the students.
        """
        self.data[self.id_counter] = data
        self.id_counter += 1

        return self.id_counter - 1

    def read(self, _id: int) -> dict:
        return self.data[_id]

    def update(self, _id, data) -> None:
        self.data[_id] = data

    def delete(self, _id: int) -> None:
        del self.data[_id]

    def get_all_data(self) -> dict:
        return self.data
    
    def count(self) -> int:
        return len(self.data)
