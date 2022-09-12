import click

from client.models.clinic_history.service_clinic_history import ClinicHistoryService
from client.models.clinic_history.clinic_history import ClinicHistory
from client.models.people.services.service_users import UserService
from client.models.attention.services.service_appointments import AppointmentService
from client.models.attention.services.service_hospitalizations import HospitalizationService

USERS_TABLE = '.users.csv'
APPOINTMENTS_TABLE = '.appointments.csv'
HOSPITALIZATIONS_TABLE = '.hospitalizations.csv'

@click.group()
def clinic_histories():
  """Administra el CRUD de historias clinicas"""
  pass


@clinic_histories.command()
@click.option('-u', '--user_id',
              type=str,
              prompt=True,
              help='Id del usuario')
@click.pass_context
def create(ctx, user_id):
  """Registra una nueva historia clinica"""

  user_service = UserService(USERS_TABLE)
  user = [user for user in user_service.read_users() if user['uid'] == user_id]

  appointment_service = AppointmentService(APPOINTMENTS_TABLE)
  appointments = [appointment for appointment in appointment_service.read_appointments() if appointment['user_id'] == user_id]

  hospitalization_service = HospitalizationService(HOSPITALIZATIONS_TABLE)
  hospitalizations = [hospitalization for hospitalization in hospitalization_service.read_hospitalizations() if hospitalization['user_id'] == user_id]


  if user:
    clinic_history = ClinicHistory(user_id, user, appointments, hospitalizations)
    clinic_history_service = ClinicHistoryService(ctx.obj['clinic_histories_table'])

    clinic_history_service.create_clinic_history(clinic_history)
  else:
    click.echo("Id de usuario no valido")


@clinic_histories.command()
@click.pass_context
def read(ctx):
  """Lee todas las historias clinicas"""
  clinic_history_service = ClinicHistoryService(ctx.obj['clinic_histories_table'])

  clinic_histories = clinic_history_service.read_clinic_histories()

  click.echo('ID | UserId | UserInfo | Appointments | Hospitalizations')
  click.echo('-' * 80)
  for clinic_history in clinic_histories:
    click.echo('{uid} | {user_id} | {user} | {appointments} | {hospitalizations}'.format(
      uid=clinic_history['uid'],
      user_id=clinic_history['user_id'],
      user=clinic_history['user_info'],
      appointments=clinic_history['appointments'],
      hospitalizations=clinic_history['hospitalizations']
    ))

@clinic_histories.command()
@click.argument('user_id', type=str)
@click.pass_context
def get_clinic_history_by_user_id(ctx, user_id):
  """Arroja la historia clinica del usuario por id"""
  clinic_history_service = ClinicHistoryService(ctx.obj['clinic_histories_table'])

  clinic_histories = clinic_history_service.read_clinic_histories()

  clinic_history_by_user_id = [clinic_history_by_user_id for clinic_history_by_user_id in clinic_histories if clinic_history_by_user_id['user_id'] == user_id]

  click.echo('ID | UserId | UserInfo | Appointments | Hospitalizations')
  click.echo('-' * 80) 
  for clinic_history in clinic_history_by_user_id:
    click.echo('{uid} | {user_id} | {user} | {appointments} | {hospitalizations}'.format(
      uid=clinic_history['uid'],
      user_id=clinic_history['user_id'],
      user=clinic_history['user_info'],
      appointments=clinic_history['appointments'],
      hospitalizations=clinic_history['hospitalizations']
    ))


@clinic_histories.command()
@click.argument('clinic_history_uid', type=str)
@click.pass_context
def update(ctx, clinic_history_uid):
  """Actualiza una historia clinica"""
  clinic_history_service = ClinicHistoryService(ctx.obj['clinic_histories_table'])
  clinic_history = [clinic_history for clinic_history in clinic_history_service.read_clinic_histories() if clinic_history['uid'] == clinic_history_uid]

  if clinic_history:
    clinic_history = _update_clinic_history_flow(ClinicHistory(**clinic_history[0]))
    clinic_history_service.update_clinic_history(clinic_history)

    click.echo('Historia clinica actualizada')
  else:
    click.echo('Historia clinica no encontrada...')


def _update_clinic_history_flow(clinic_history):
  click.echo('Dejar el campo en blanco si no desea modificar el valor')

  clinic_history.user_id = click.prompt('Nuevo id de usuario: ', type=str, default=clinic_history.user_id)


  return clinic_history


@clinic_histories.command()
@click.argument('clinic_history_uid', type=str)
@click.pass_context
def delete(ctx, clinic_history_uid):
  """Elimina una historia clinica"""
  clinic_history_service = ClinicHistoryService(ctx.obj['clinic_histories_table'])

  if click.confirm('Está seguro que desea eliminar la historia clinica con id: {}'.format(clinic_history_uid)):
    clinic_history_service.delete_clinic_history(clinic_history_uid)

all = clinic_histories