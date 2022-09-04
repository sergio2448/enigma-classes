from client.common.services import CRUDService
from client.models.attention.hospitalizations import Hospitalization

class HospitalizationService(CRUDService):

  def __init__(self, table_name):
    super().__init__(table_name)

  def create_hospitalization(self,hospitalization):
    self.create(hospitalization.to_dict(), Hospitalization.schema())

  def read_hospitalizations(self):
    return self.read(Hospitalization.schema())

  def update_hospitalization(self, updated_hospitalization):
    self.update(updated_hospitalization.to_dict(), Hospitalization.schema()) #revisar

  def delete_hospitalization(self, hospitalization_uid):
    self.delete(hospitalization_uid, Hospitalization.schema())