from client.common.generate_id import Id

class Medicine(Id):

  def __init__(self, name, amount, uid=None):
    super().__init__(uid)
    self.name = name
    self.amount = amount

  @staticmethod
  def schema():
    return ['name', 'amount', 'uid']