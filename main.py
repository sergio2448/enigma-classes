import click

from client.commands import users_commands, doctors_commands, hospitalizations_commands, appointments_commands, medicines_commands, clinic_histories_commands

USERS_TABLE = '.users.csv'
DOCTORS_TABLE = '.doctors.csv'
HOSPITALIZATIONS_TABLE = '.hospitalizations.csv'
APPOINTMENTS_TABLE = 'appointments.csv'
MEDICINES_TABLE = 'medicines.csv'
CLINIC_HISTORIES_TABLE = 'clinic_histories.csv'

@click.group()
def tables():
  """Python App CLI"""
  pass

@tables.group()
@click.pass_context
def us(ctx):
  """Opciones tabla de Usuarios."""
  ctx.obj = {}
  ctx.obj['users_table'] = USERS_TABLE
us.add_command(users_commands.all)

@tables.group()
@click.pass_context
def dc(ctx):
  """Opciones tabla de Doctores."""
  ctx.obj = {}
  ctx.obj['doctors_table'] = DOCTORS_TABLE
dc.add_command(doctors_commands.all)

@tables.group()
@click.pass_context
def hs(ctx):
  """Opciones tabla de Hospitalizaciones."""
  ctx.obj = {}
  ctx.obj['hospitalizations_table'] = HOSPITALIZATIONS_TABLE
hs.add_command(hospitalizations_commands.all)

@tables.group()
@click.pass_context
def ap(ctx):
  """Opciones tabla de Citas."""
  ctx.obj = {}
  ctx.obj['appointments_table'] = APPOINTMENTS_TABLE
ap.add_command(appointments_commands.all)

@tables.group()
@click.pass_context
def md(ctx):
  """Opciones tabla de Medicamentos."""
  ctx.obj = {}
  ctx.obj['medicines_table'] = MEDICINES_TABLE
md.add_command(medicines_commands.all)

@tables.group()
@click.pass_context
def hc(ctx):
  """Opciones tabla de Historias clinicas."""
  ctx.obj = {}
  ctx.obj['clinic_histories_table'] = CLINIC_HISTORIES_TABLE
hc.add_command(clinic_histories_commands.all)


if __name__ == '__main__':
  tables()

  