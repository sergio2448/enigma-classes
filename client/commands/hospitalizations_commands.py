import click

from client.models.attention.services.service_hospitalizations import HospitalizationService
from client.models.attention.hospitalizations import Hospitalization


@click.group()
def hospitalizations():
  """Administra el CRUD de hospitalizaciones"""
  pass


@hospitalizations.command()
@click.option('-u', '--user_id',
              type=str,
              prompt=True,
              help='Id del usuario')
@click.option('-i', '--date_init',
              type=str,
              prompt=True,
              help='Fecha de inicio')
@click.option('-f', '--date_finish',
              type=str,
              prompt=True,
              help='Fecha de finalizacion')
@click.pass_context
def create(ctx, user_id, date_init, date_finish):
  """Crea una nueva hospitalizacion"""
  hospitalization = Hospitalization(user_id, date_init, date_finish)
  hospitalization_service = HospitalizationService(ctx.obj['hospitalizations_table'])

  hospitalization_service.create_hospitalization(hospitalization)


@hospitalizations.command()
@click.pass_context
def read(ctx):
  """Lee todas las hospitalizaciones"""
  hospitalization_service = HospitalizationService(ctx.obj['hospitalizations_table'])

  hospitalizations = hospitalization_service.read_hospitalizations()

  click.echo('ID | UserId | DateInit | DateFinish')
  click.echo('-' * 80)
  for hospitalization in hospitalizations:
    click.echo('{uid} | {user_id} | {date_init} | {date_finish}'.format(
      uid=hospitalization['uid'],
      user_id=hospitalization['user_id'],
      date_init=hospitalization['date_init'],
      date_finish=hospitalization['date_finish'],
    ))


@hospitalizations.command()
@click.argument('hospitalization_uid', type=str)
@click.pass_context
def update(ctx, hospitalization_uid):
  """Actualiza una hospitalizacion"""
  hospitalization_service = HospitalizationService(ctx.obj['hospitalizations_table'])
  hospitalization = [hospitalization for hospitalization in hospitalization_service.read_hospitalizations() if hospitalization['uid'] == hospitalization_uid]

  if hospitalization:
    hospitalization = _update_hospitalization_flow(Hospitalization(**hospitalization[0]))
    hospitalization_service.update_hospitalization(hospitalization)

    click.echo('Hospitalizacion actualizada')
  else:
    click.echo('Hospitalizacion no encontrada...')


def _update_hospitalization_flow(hospitalization):
  click.echo('Dejar el campo en blanco si no desea modificar el valor')

  hospitalization.user_id = click.prompt('Nuevo id de usuario: ', type=str, default=hospitalization.user_id)
  hospitalization.date_init = click.prompt('Nueva fecha de ingreso: ', type=str, default=hospitalization.date_init)
  hospitalization.date_finish = click.prompt('Nueva fecha de salida: ', type=str, default=hospitalization.date_finish)


  return hospitalization


@hospitalizations.command()
@click.argument('hospitalization_uid', type=str)
@click.pass_context
def delete(ctx, hospitalization_uid):
  """Elimina una hospitalizacion"""
  hospitalization_service = HospitalizationService(ctx.obj['hospitalizations_table'])

  if click.confirm('Está seguro que desea eliminar la hospitalizacion con id: {}'.format(hospitalization_uid)):
    hospitalization_service.delete_hospitalization(hospitalization_uid)

all = hospitalizations