from client.models.people.people import Person

class User(Person):

  def __init__(self, name, email, cc, gender, eps, state, blood_type, uid=None):
    super().__init__(name, email, cc, gender, uid)
    self.eps = eps
    self.state = state
    self.blood_type = blood_type

  @staticmethod
  def schema():
    return ['name', 'email', 'cc', 'gender', 'eps', 'state', 'blood_type', 'uid']
