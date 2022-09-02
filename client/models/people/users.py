from client.models.people.people import Person

class User(Person):

  def __init__(self, name, email, cc, gender, eps, state, uid=None):
    super().__init__(name, email, cc, gender, uid)
    self.eps = eps
    self.state = state

  @staticmethod
  def schema():
    return ['name', 'email', 'cc', 'gender', 'eps', 'state', 'uid']
