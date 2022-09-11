import abc
import csv
import os

class CRUDService(abc.ABC):
  """Crud general que interactúa con el sistema operativo administrando los csv"""
  def __init__(self, table_name):
    self.table_name = table_name

  
  def create(self, row, schema):
    """Recibe el esquema (que es quien contiene las columnas del csv) y la fila a almacenar (row = diccionario, schema = lista de strings)"""
    with open(self.table_name, mode='a') as f:
      writer = csv.DictWriter(f, fieldnames=schema)
      writer.writerow(row)    


  def read(self, schema):
    """Abre el csv indicado en table_name como modo lectura y retorna una lista con la información almacenada en los campos (schema = lista de strings)"""
    with open(self.table_name, mode='r') as f:
      reader = csv.DictReader(f, fieldnames=schema)

      return list(reader)


  def update(self, updated_row, schema):
    """Recibe una nueva fila (updated_row = diccionario, schema = lista de strings)"""
    rows = self.read(schema)

    updated_rows = []
    for row in rows:
      if row['uid'] == updated_row['uid']:
        updated_rows.append(updated_row)
      else:
        updated_rows.append(row)

    self._save_to_disk(updated_rows, schema)


  def delete(self, row_uid, schema):
    """(row_uid = string, schema = lista de strings)"""
    rows = self.read(schema)
    updated_rows = [row for row in rows if row['uid'] != row_uid]

    self._save_to_disk(updated_rows, schema)


  def _save_to_disk(self, rows, schema):
    """(rows = diccionario, schema = lista de strings) se genera un csv temporal (tmp_table_name) que sirve de puente para eliminar o actualizar datos en el csv original, luego se elimina el csv original y se renombra el csv temporal como el inicial"""
    tmp_table_name = self.table_name + '.tmp'

    with open(tmp_table_name, mode='w') as f:
      writer = csv.DictWriter(f, fieldnames=schema)
      writer.writerows(rows)

    os.remove(self.table_name)
    os.rename(tmp_table_name, self.table_name)
    