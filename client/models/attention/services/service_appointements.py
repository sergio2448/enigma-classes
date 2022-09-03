from client.common.services import CRUDService
from client.models.attention.appointments import Appointment

class ServiceAppointments(CRUDService):

  def __init__(self, table_name):
    super().__init__(table_name)

  def create_appointment(self,appointment):
    self.create(appointment.to_dict(), Appointment.schema())

  def read_users(self):
    return self.read(Appointment.schema())

  def update_user(self, updated_appointment):
    self.update(updated_appointment.to_dict(), Appointment.schema()) #revisar

  def delete_user(self, appointment_id):
    self.delete(appointment_id, Appointment.schema())
    