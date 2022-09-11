from client.common.services import CRUDService
from client.models.attention.appointments import Appointment

class AppointmentService(CRUDService):
  """AppointmentService personaliza el crud de la clase Appointment, en table_name recibimos el nombre del csv que almacenará los datos"""
  def __init__(self, table_name):
    super().__init__(table_name)

  def create_appointment(self, appointment):
    self.create(appointment.to_dict(), Appointment.schema())

  def read_appointments(self):
    return self.read(Appointment.schema())

  def update_appointment(self, updated_appointment):
    self.update(updated_appointment.to_dict(), Appointment.schema()) #revisar

  def delete_appointment(self, appointment_uid):
    self.delete(appointment_uid, Appointment.schema())