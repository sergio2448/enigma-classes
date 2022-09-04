import click

from client.models.people.services.service_doctor import DoctorService
from client.models.people.doctors import Doctor


@click.group()
def doctors():
  """Administra el CRUD de doctores"""
  pass


@doctors.command()
@click.option('-n', '--name',
              type=str,
              prompt=True,
              help='El nombre del doctor')
@click.option('-e', '--email',
              type=str,
              prompt=True,
              help='El correo del doctor')
@click.option('-c', '--cc',
              type=str,
              prompt=True,
              help='Número de identificación del doctor')
@click.option('-g', '--gender',
              type=str,
              prompt=True,
              help='Sexo del doctor')
@click.option('-sp', '--specialty',
              type=str,
              prompt=True,
              help='Especialidad del doctor')
@click.pass_context
def create(ctx, name, email, cc, gender, specialty):
  """Crea un nuevo doctor"""
  doctor = Doctor(name, email, cc, gender, specialty)
  doctor_service = DoctorService(ctx.obj['doctors_table'])

  doctor_service.create_doctor(doctor)


@doctors.command()
@click.pass_context
def read(ctx):
  """Lee todos los doctores"""
  doctor_service = DoctorService(ctx.obj['doctors_table'])

  doctors = doctor_service.read_doctors()

  click.echo('ID | Name | Email | CC | Gender | Specialty')
  click.echo('-' * 80)
  for doctor in doctors:
    click.echo('{uid} | {name} | {email} | {cc} | {gender} | {specialty}'.format(
      uid=doctor['uid'],
      name=doctor['name'],
      email=doctor['email'],
      cc=doctor['cc'],
      gender=doctor['gender'],
      specialty=doctor['specialty'],
    ))


@doctors.command()
@click.argument('doctor_uid', type=str)
@click.pass_context
def update(ctx, doctor_uid):
  """Actualiza un doctor"""
  doctor_service = DoctorService(ctx.obj['doctors_table'])
  doctor = [doctor for doctor in doctor_service.read_doctors() if doctor['uid'] == doctor_uid]

  if doctor:
    doctor = _update_doctor_flow(Doctor(**doctor[0]))
    doctor_service.update_doctor(doctor)

    click.echo('Doctor actualizado')
  else:
    click.echo('Doctor no encontrado...')


def _update_doctor_flow(doctor):
  click.echo('Dejar el campo en blanco si no desea modificar el valor')

  doctor.name = click.prompt('Nuevo nombre: ', type=str, default=doctor.name)
  doctor.email = click.prompt('Nuevo email: ', type=str, default=doctor.email)
  doctor.cc = click.prompt('Nuevo CC: ', type=str, default=doctor.cc)
  doctor.gender = click.prompt('Nuevo sexo: ', type=str, default=doctor.gender)
  doctor.specialty = click.prompt('Nueva EPS: ', type=str, default=doctor.specialty)


  return doctor


@doctors.command()
@click.argument('doctor_uid', type=str)
@click.pass_context
def delete(ctx, doctor_uid):
  """Elimina un doctor"""
  doctor_service = DoctorService(ctx.obj['doctors_table'])

  if click.confirm('Está seguro que desea eliminar el usuario con id: {}'.format(doctor_uid)):
    doctor_service.delete_doctor(doctor_uid)

all = doctors
    