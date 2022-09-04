import click

from client.commands import users_commands, doctors_commands, hospitalizations_commands

USERS_TABLE = '.users.csv'
DOCTORS_TABLE = '.doctors.csv'
HOSPITALIZATIONS_TABLE = '.hospitalizations.csv'

@click.group()
def tables():
  """Python App CLI"""
  pass

@tables.group()
@click.pass_context
def us(ctx):
  """Administra el CRUD de usuarios."""
  ctx.obj = {}
  ctx.obj['users_table'] = USERS_TABLE
us.add_command(users_commands.all)

@tables.group()
@click.pass_context
def dc(ctx):
  """Administra el CRUD de doctores."""
  ctx.obj = {}
  ctx.obj['doctors_table'] = DOCTORS_TABLE
dc.add_command(doctors_commands.all)

@tables.group()
@click.pass_context
def hs(ctx):
  """Administra el CRUD de hospitalizaciones."""
  ctx.obj = {}
  ctx.obj['hospitalizations_table'] = HOSPITALIZATIONS_TABLE
hs.add_command(hospitalizations_commands.all)


if __name__ == '__main__':
  tables()

  