# Hospital UdeA

_Se generan los objetos que representan las entidades de negocio de un hospital que esta desarrollando su sistema para atención de pacientes._

## Diagrama 📁
![Diagrama](https://user-images.githubusercontent.com/84557725/190803899-2eb14414-0669-4bb6-897b-40ca6173500f.png)


### Instalación y ejecución 🔧

_Se sugiere el uso de un entorno virtual [venv](https://docs.python.org/es/3/tutorial/venv.html)_

_Una vez activado el entorno virtual corremos el siguiente comando para instalar requerimientos:_

```
python -m pip install -r requirements.txt
```

_Corremos el archivo **main.py** para ver las opciones disponibles_

```
python main.py
```

_Para crear un usuario se ejecuta la siguiente ruta:_

```
python main.py us users create
```
_Cambiando el verbo **create** a **update**, **delete** o **read** podemos obtener las cuatro acciones de un CRUD, éstas estan implementadas en todos los objetos._

_Para generar la historia clínica de un usuario ejecutamos:_

```
python main.py hc clinic-histories get-clinic-history-by-user-id 'user_id'
```

## Construido con 🛠️

* [Click](https://click.palletsprojects.com/en/8.1.x/) - Usado para generar una interfaz de línea de comandos.

## Autores ✒️

* **Randolph Peralta** - [RandolphPeralta](https://github.com/RandolphPeralta)
* **Carolina Lopera** - [CarolinaLop](https://github.com/CarolinaLop)
* **Mateo Soto** - [MateoSA99](https://github.com/MateoSA99)
* **Sergio Arbelaez** - [sergio2448](https://github.com/sergio2448)
