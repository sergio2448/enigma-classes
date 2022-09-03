class hospitalizations:
    def __init__(self, user_id, date_init, date_finish):
        self.user_id =user_id
        self.date_init = date_init
        self.date_finish = date_finish

    @staticmethod
    def schema():
        return ['user_id', 'date_init', 'date_fisish']#falta ponerle datos