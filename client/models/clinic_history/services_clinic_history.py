from client.common.services import CRUDService
from client.models.clinic_history.clinic_history import ClinicHistory

class ClinicHistoryService(CRUDService):

  def __init__(self, table_name):
    super().__init__(table_name)

  def create_clinic_history(self,user_id):
    self.create(user_id.to_dict(), ClinicHistory.schema())

  def read_users(self):
    return self.read(ClinicHistory.schema())

  def update_user(self, updated_user):
    self.update(updated_user.to_dict(), ClinicHistory.schema()) #revisar

  def delete_user(self, user_uid):
    self.delete(user_uid, ClinicHistory.schema())