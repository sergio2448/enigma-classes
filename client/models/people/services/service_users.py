from client.common.services import CRUDService
from client.models.people.users import User

class UserService(CRUDService):

  def __init__(self, table_name):
    super().__init__(table_name)

  def create_user(self, user):
    self.create(user.to_dict(), User.schema())

  def read_users(self):
    return self.read(User.schema())

  def update_user(self, updated_user):
    self.update(updated_user.to_dict(), User.schema())

  def delete_user(self, user_uid):
    self.delete(user_uid, User.schema())
