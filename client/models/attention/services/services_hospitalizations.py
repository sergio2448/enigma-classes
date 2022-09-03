from client.common.services import CRUDService
from client.models.attention.hospitalizations import hospitalizations

class ServiceHospitalizations(CRUDService):

  def __init__(self, table_name):
    super().__init__(table_name)

  def create_hospitalizations(self,hospitalizations):
    self.create(hospitalizations.to_dict(), hospitalizations.schema())

  def read_hospitalizations(self):
    return self.read(hospitalizations.schema())

  def update_user(self, updated_hospitalizations):
    self.update(updated_hospitalizations.to_dict(), hospitalizations.schema()) #revisar

  def delete_user(self, hospitalizations_id):
    self.delete(hospitalizations_id,hospitalizations.schema())