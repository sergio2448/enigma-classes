from client.models.people.services.service_users import UserService
from client.models.people.users import User

from client.models.people.services.service_doctor import DoctorService
from client.models.people.doctors import Doctor

USERS_TABLE = '.users.csv'
DOCTORS_TABLE = '.doctors.csv'

def create_user(name, email, cc, gender, eps, state):
  user = User(name, email, cc, gender, eps, state)
  user_service = UserService(USERS_TABLE)

  user_service.create_user(user)


def create_doctor(name, email, cc, gender, specialty):
  doctor = Doctor(name, email, cc, gender, specialty)
  doctor_service = DoctorService(DOCTORS_TABLE)

  doctor_service.create_doctor(doctor)


if __name__ == '__main__':
  person = input("Escriba u para ingresar un usuario, d para ingresar un doctor: ")

  if person == 'u':
    user_name = input("Nombre: ")
    user_email = input("Email: ")
    user_cc = input("CC: ")
    user_gender = input("Sexo: ")
    user_eps = input("EPS: ")
    user_state = input("Estado: ")

    create_user(user_name, user_email, user_cc, user_gender, user_eps, user_state)
  
  elif person == 'd':
    doctor_name = input("Nombre: ")
    doctor_email = input("Email: ")
    doctor_cc = input("CC: ")
    doctor_gender = input("Sexo: ")
    doctor_specialty = input("Especialidad: ")

    create_doctor(doctor_name, doctor_email, doctor_cc, doctor_gender, doctor_specialty)

  else:
    print("Parámetro invalido...")