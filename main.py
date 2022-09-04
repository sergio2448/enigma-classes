import click

from client.models.people.services.service_users import UserService
from client.models.people.users import User

from client.models.people.services.service_doctor import DoctorService
from client.models.people.doctors import Doctor

from client.commands import users_commands
from client.commands import doctors_commands

USERS_TABLE = '.users.csv'
DOCTORS_TABLE = '.doctors.csv'

@click.group()
@click.pass_context
def us(ctx):
  """Administra el CRUD de usuarios."""
  ctx.obj = {}
  ctx.obj['users_table'] = USERS_TABLE

@click.group()
@click.pass_context
def dc(ctx):
  """Administra el CRUD de doctores."""
  ctx.obj = {}
  ctx.obj['doctors_table'] = DOCTORS_TABLE
  
dc.add_command(doctors_commands.all)
us.add_command(users_commands.all)


if __name__ == '__main__':
  dc()

  