import abc
import uuid

class Id(abc.ABC):
  """Clase abstracta para generar ids aleatorios a todas las clases"""
  
  def __init__(self, uid=None):
    self.uid = uid or uuid.uuid4()

  def to_dict(self):
    return vars(self)

  @staticmethod
  @abc.abstractmethod
  def schema():
    pass