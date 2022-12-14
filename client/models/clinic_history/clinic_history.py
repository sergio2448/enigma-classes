from client.common.generate_id import Id
class ClinicHistory(Id):

  def __init__(self, user_id, user_info, appointments, hospitalizations, uid=None):
    super().__init__(uid)
    self.user_id = user_id
    self.user_info = user_info
    self.appointments = appointments
    self.hospitalizations = hospitalizations

  @staticmethod
  def schema():
    return ['user_id', 'user_info', 'appointments', 'hospitalizations', 'uid'] #appointments y user_info son dicts