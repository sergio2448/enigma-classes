import click

from client.models.medicines.service_medicines import MedicineService
from client.models.medicines.medicines import Medicine


@click.group()
def medicines():
  """Administra el CRUD de medicamentos"""
  pass


@medicines.command()
@click.option('-n', '--name',
              type=str,
              prompt=True,
              help='Nombre del medicamento')
@click.option('-a', '--amount',
              type=str,
              prompt=True,
              help='Cantidad')
@click.pass_context
def create(ctx, name, amount):
  """Registra un nuevo medicamento"""
  medicine = Medicine(name, amount)
  medicine_service = MedicineService(ctx.obj['medicines_table'])

  medicine_service.create_medicine(medicine)


@medicines.command()
@click.pass_context
def read(ctx):
  """Lee todos los medicamentos"""
  medicine_service = MedicineService(ctx.obj['medicines_table'])

  medicines = medicine_service.read_medicines()

  click.echo('ID | Name | Amount')
  click.echo('-' * 80)
  for medicine in medicines:
    click.echo('{uid} | {name} | {amount}'.format(
      uid=medicine['uid'],
      name=medicine['name'],
      amount=medicine['amount'],
    ))


@medicines.command()
@click.argument('medicine_uid', type=str)
@click.pass_context
def update(ctx, medicine_uid):
  """Actualiza un medicamento"""
  medicine_service = MedicineService(ctx.obj['medicines_table'])
  medicine = [medicine for medicine in medicine_service.read_medicines() if medicine['uid'] == medicine_uid]

  if medicine:
    medicine = _update_medicine_flow(Medicine(**medicine[0]))
    medicine_service.update_medicine(medicine)

    click.echo('Medicamento actualizado')
  else:
    click.echo('Medicamento no encontrado...')


def _update_medicine_flow(medicine):
  click.echo('Dejar el campo en blanco si no desea modificar el valor')

  medicine.name = click.prompt('Nuevo nombre: ', type=str, default=medicine.name)
  medicine.amount = click.prompt('Nueva cantidad: ', type=str, default=medicine.amount)


  return medicine


@medicines.command()
@click.argument('medicine_uid', type=str)
@click.pass_context
def delete(ctx, medicine_uid):
  """Elimina un medicamento"""
  medicine_service = MedicineService(ctx.obj['medicines_table'])

  if click.confirm('Está seguro que desea eliminar el medicamento con id: {}'.format(medicine_uid)):
    medicine_service.delete_medicine(medicine_uid)

all = medicines