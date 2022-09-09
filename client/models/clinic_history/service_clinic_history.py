from client.common.services import CRUDService
from client.models.clinic_history.clinic_history import ClinicHistory

class ClinicHistoryService(CRUDService):

  def __init__(self, table_name):
    super().__init__(table_name)

  def create_clinic_history(self, clinic_history):
    self.create(clinic_history.to_dict(), ClinicHistory.schema())

  def read_clinic_histories(self):
    return self.read(ClinicHistory.schema())

  def update_clinic_history(self, updated_clinic_history):
    self.update(updated_clinic_history.to_dict(), ClinicHistory.schema()) #revisar

  def delete_clinic_history(self, clinic_history_uid):
    self.delete(clinic_history_uid, ClinicHistory.schema())
