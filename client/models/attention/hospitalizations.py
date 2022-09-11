from client.common.generate_id import Id

class Hospitalization(Id):
  def __init__(self, user_id, date_init, date_finish, reason, doctor_id, medicine_id, uid=None):
    super().__init__(uid)
    self.user_id =user_id
    self.date_init = date_init
    self.date_finish = date_finish
    self.reason = reason
    self.doctor_id = doctor_id
    self.medicine_id = medicine_id

  @staticmethod
  def schema():
    return ['user_id', 'date_init', 'date_finish', 'reason', 'doctor_id', 'medicine_id', 'uid']#falta ponerle datos