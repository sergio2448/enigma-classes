from client.common.generate_id import Id
class ClinicHistory(Id):

  def __init__(self, user_id, uid=None):
    super().__init__(uid)
    self.user_id = user_id

  @staticmethod
  def schema():
    return ['user_id', 'uid'] #appointments es dict