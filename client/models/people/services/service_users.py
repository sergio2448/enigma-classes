from client.common.services import CRUDService
from client.models.people.users import User

class UserService(CRUDService):
  """UserService personaliza el crud de la clase User, en table_name recibimos el nombre del csv que almacenará los datos"""

  def __init__(self, table_name):
    super().__init__(table_name)

  def create_user(self, user):
    """Recibe una instancia de la clase User y la envía como diccionario junto a su esquema al crud general CRUDService"""
    self.create(user.to_dict(), User.schema())

  def read_users(self):
    """Expone lo que arroja el método read de CRUDService al usarlo con el esquema de usuario"""
    return self.read(User.schema())

  def update_user(self, updated_user):
    """Recibe una instancia de la clase User"""
    self.update(updated_user.to_dict(), User.schema())

  def delete_user(self, user_uid):
    self.delete(user_uid, User.schema())
