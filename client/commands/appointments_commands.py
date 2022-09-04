import click

from client.models.attention.services.service_appointments import AppointmentService
from client.models.attention.appointments import Appointment


@click.group()
def appointments():
  """Administra el CRUD de citas"""
  pass


@appointments.command()
@click.option('-u', '--user_id',
              type=str,
              prompt=True,
              help='Id del usuario')
@click.option('-d', '--doctor_id',
              type=str,
              prompt=True,
              help='Id del doctor')
@click.option('-dt', '--date',
              type=str,
              prompt=True,
              help='Fecha de la cita')
@click.option('-t', '--time',
              type=str,
              prompt=True,
              help='Hora de la cita')
@click.option('-p', '--place',
              type=str,
              prompt=True,
              help='Lugar de la cita')
@click.option('-r', '--reason',
              type=str,
              prompt=True,
              help='Razon de la cita')
@click.option('-pr', '--prescription',
              type=str,
              prompt=True,
              help='Prescripcion')
@click.option('-s', '--state',
              type=str,
              prompt=True,
              help='Estado')
@click.pass_context
def create(ctx, user_id, doctor_id, date, time, place, reason, prescription, state):
  """Crea una nueva cita"""
  appointment = Appointment(user_id, doctor_id, date, time, place, reason, prescription, state)
  appointment_service = AppointmentService(ctx.obj['appointments_table'])

  appointment_service.create_appointment(appointment)


@appointments.command()
@click.pass_context
def read(ctx):
  """Lee todas las citas"""
  appointment_service = AppointmentService(ctx.obj['appointments_table'])

  appointments = appointment_service.read_appointments()

  click.echo('ID | UserId | DoctorId | Date | Time | Place | Reason | Prescription| State')
  click.echo('-' * 80)
  for appointment in appointments:
    click.echo('{uid} | {user_id} | {doctor_id} | {date} | {time} | {place} | {reason} | {prescription} | {state}'.format(
      uid=appointment['uid'],
      user_id=appointment['user_id'],
      doctor_id=appointment['doctor_id'],
      date=appointment['date'],
      time=appointment['time'],
      place=appointment['place'],
      reason=appointment['reason'],
      prescription=appointment['prescription'],
      state=appointment['state']
    ))


@appointments.command()
@click.argument('appointment_uid', type=str)
@click.pass_context
def update(ctx, appointment_uid):
  """Actualiza una cita"""
  appointment_service = AppointmentService(ctx.obj['appointments_table'])
  appointment = [appointment for appointment in appointment_service.read_appointments() if appointment['uid'] == appointment_uid]

  if appointment:
    appointment = _update_appointment_flow(Appointment(**appointment[0]))
    appointment_service.update_appointment(appointment)

    click.echo('Cita actualizada')
  else:
    click.echo('Cita no encontrada...')


def _update_appointment_flow(appointment):
  click.echo('Dejar el campo en blanco si no desea modificar el valor')

  appointment.user_id = click.prompt('Nuevo id de usuario: ', type=str, default=appointment.user_id)
  appointment.doctor_id = click.prompt('Nuevo id de doctor: ', type=str, default=appointment.doctor_id)
  appointment.date = click.prompt('Nueva fecha: ', type=str, default=appointment.date)
  appointment.time = click.prompt('Nueva hora: ', type=str, default=appointment.time)
  appointment.place = click.prompt('Nuevo lugar: ', type=str, default=appointment.place)
  appointment.reason = click.prompt('Nueva razon: ', type=str, default=appointment.reason)
  appointment.prescription = click.prompt('Nueva prescripcion: ', type=str, default=appointment.prescription)
  appointment.state = click.prompt('Nuevo estado: ', type=str, default=appointment.state)


  return appointment


@appointments.command()
@click.argument('appointment_uid', type=str)
@click.pass_context
def delete(ctx, appointment_uid):
  """Elimina una cita"""
  appointment_service = AppointmentService(ctx.obj['appointments_table'])

  if click.confirm('Está seguro que desea eliminar la cita con id: {}'.format(appointment_uid)):
    appointment_service.delete_appointment(appointment_uid)

all = appointments