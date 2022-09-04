class ClinicHistory:
    def __init__(self, user_id):
        self.user_id = user_id

    @staticmethod
    def schema():
        return ['id', 'user_id', 'cc', 'name', 'eps', 'state', 'appoinments'] #appointments es dict