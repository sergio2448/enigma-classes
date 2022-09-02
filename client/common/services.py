import abc
import csv
import os

class CRUDService(abc.ABC):

  def __init__(self, table_name):
    self.table_name = table_name

  
  def create(self, row, schema):
    with open(self.table_name, mode='a') as f:
      writer = csv.DictWriter(f, fieldnames=schema)
      writer.writerow(row)    


  def read(self, schema):
    with open(self.table_name, mode='r') as f:
      reader = csv.DictReader(f, fieldnames=schema)

      return read(reader)


  def update(self, updated_row, schema):
    rows = self.read(schema)

    updated_rows = []
    for row in rows:
      if row['uid'] == updated_row['uid']:
        updated_rows.append(updated_row)
      else:
        updated_rows.append(row)

    self._save_to_disk(updated_rows, schema)


  def delete(self, row_uid, schema):
    rows = self.read(schema)
    updated_rows = [row for row in rows if row['uid'] != row_uid]

    self._save_to_disk(updated_rows, schema)


  def _save_to_disk(self, rows, schema):
    tmp_table_name = self.table_name + '.tmp'

    with open(tmp_table_name, mode='w') as f:
      writer = csv.DictWriter(f, fieldnames=schema)
      writer.writerows(rows)

    os.remove(self.table_name)
    os.rename(tmp_table_name, self.table_name)
    