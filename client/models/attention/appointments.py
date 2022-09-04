from client.common.generate_id import Id

class Appointment(Id):
    def __init__(self, user_id, doctor_id, date, time, place, reason, uid):
        super().__init__(uid)
        self.user_id = user_id
        self.doctor_id = doctor_id
        self.date = date
        self.time = time     
        self.place = place
        self.reason = reason
        self.prescription = ''
        self.state = 'Pendiente'

    @staticmethod
    def schema():
        return ['user_id', 'doctor_id', 'date', 'time', 'place', 'reason', 'prescription', 'state', 'uid']