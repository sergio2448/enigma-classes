from client.common.generate_id import Id

class Person(Id):

  def __init__(self, name, email, cc, gender, uid=None):
    super().__init__(uid)
    self.name = name
    self.email = email
    self.cc = cc
    self.gender = gender