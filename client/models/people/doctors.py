from client.models.people.people import Person

class Doctor(Person):

  def __init__(self, name, email, cc, gender, specialty, uid=None):
    super().__init__(name, email, cc, gender, uid)
    self.specialty = specialty

  @staticmethod
  def schema():
    return ['name', 'email', 'cc', 'gender', 'specialty', 'uid']