from client.common.services import CRUDService
from client.models.people.doctors import Doctor

class DoctorService(CRUDService):

  def __init__(self, table_name):
    super().__init__(table_name)

  def create_doctor(self, doctor):
    self.create(doctor.to_dict(), Doctor.schema())

  def read_doctors(self):
    return self.read(Doctor.schema())

  def update_doctor(self, updated_doctor):
    self.update(updated_doctor.to_dict(), Doctor.schema())

  def delete_doctor(self, doctor_uid):
    self.delete(doctor_uid, Doctor.schema())