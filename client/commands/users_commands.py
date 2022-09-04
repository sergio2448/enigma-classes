import click

from client.models.people.services.service_users import UserService
from client.models.people.users import User


@click.group()
def users():
  """Administra el CRUD de usuarios"""
  pass


@users.command()
@click.option('-n', '--name',
              type=str,
              prompt=True,
              help='El nombre del usuario')
@click.option('-e', '--email',
              type=str,
              prompt=True,
              help='El correo del usuario')
@click.option('-c', '--cc',
              type=str,
              prompt=True,
              help='Número de identificación del usuario')
@click.option('-g', '--gender',
              type=str,
              prompt=True,
              help='Sexo del usuario')
@click.option('-ep', '--eps',
              type=str,
              prompt=True,
              help='EPS del usuario')
@click.option('-s', '--state',
              type=str,
              prompt=True,
              help='El estado del usuario')
@click.pass_context
def create(ctx, name, email, cc, gender, eps, state):
  """Crea un nuevo usuario"""
  user = User(name, email, cc, gender, eps, state)
  user_service = UserService(ctx.obj['users_table'])

  user_service.create_user(user)


@users.command()
@click.pass_context
def read(ctx):
  """Lee todos los usuarios"""
  user_service = UserService(ctx.obj['users_table'])

  users = user_service.read_users()

  click.echo('ID | Name | Email | CC | Gender | EPS | State')
  click.echo('-' * 80)
  for user in users:
    click.echo('{uid} | {name} | {email} | {cc} | {state}'.format(
      uid=user['uid'],
      name=user['name'],
      email=user['email'],
      cc=user['cc'],
      gender=user['gender'],
      eps=user['eps'],
      state=user['state']
    ))


@users.command()
@click.argument('user_uid', type=str)
@click.pass_context
def update(ctx, user_uid):
  """Actualiza un usuario"""
  user_service = UserService(ctx.obj['users_table'])
  user = [user for user in user_service.read_users() if user['uid'] == user_uid]

  if user:
    user = _update_user_flow(User(**user[0]))
    user_service.update_user(user)

    click.echo('Usuario actualizado')
  else:
    click.echo('Usuario no encontrado...')


def _update_user_flow(user):
  click.echo('Dejar el campo en blanco si no desea modificar el valor')

  user.name = click.prompt('Nuevo nombre: ', type=str, default=user.name)
  user.email = click.prompt('Nuevo email: ', type=str, default=user.email)
  user.cc = click.prompt('Nuevo CC: ', type=str, default=user.cc)
  user.gender = click.prompt('Nuevo sexo: ', type=str, default=user.gender)
  user.eps = click.prompt('Nueva EPS: ', type=str, default=user.eps)
  user.state = click.prompt('Nuevo estado: ', type=str, default=user.state)


  return user


@users.command()
@click.argument('user_uid', type=str)
@click.pass_context
def delete(ctx, user_uid):
  """Elimina un usuario"""
  user_service = UserService(ctx.obj['users_table'])

  if click.confirm('Está seguro que desea eliminar el usuario con id: {}'.format(user_uid)):
    user_service.delete_user(user_uid)

all = users
    