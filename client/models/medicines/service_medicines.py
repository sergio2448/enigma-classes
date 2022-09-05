from client.common.services import CRUDService
from client.models.medicines.medicines import Medicine

class MedicineService(CRUDService):

  def __init__(self, table_name):
    super().__init__(table_name)

  def create_medicine(self, medicine):
    self.create(medicine.to_dict(), Medicine.schema())

  def read_medicines(self):
    return self.read(Medicine.schema())

  def update_medicine(self, updated_medicine):
    self.update(updated_medicine.to_dict(), Medicine.schema())

  def delete_medicine(self, medicine_uid):
    self.delete(medicine_uid, Medicine.schema())