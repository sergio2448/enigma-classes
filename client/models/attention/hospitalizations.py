from client.common.generate_id import Id

class Hospitalization(Id):
  def __init__(self, user_id, date_init, date_finish, uid=None):
    super().__init__(uid)
    self.user_id =user_id
    self.date_init = date_init
    self.date_finish = date_finish

  @staticmethod
  def schema():
    return ['user_id', 'date_init', 'date_finish', 'uid']#falta ponerle datos