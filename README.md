# Gurus test

## Comenzando 🚀
Este repositorio es para albergar el backend de el test de "Requerimos que desarrolles un proyecto que detecte si una persona tiene diferencias genéticas basándose en
su secuencia de ADN"

### Pre-requisitos 📋

_Tener instalado Python, Conda y PostgreSQL_


### Instalación 🔧

1.	Clonar el repositorio.
2.	Se debe de crear un entorno virtual de conda dentro de la carpeta del repo, de sugerencia se debe de llamar guros esto se hace con el siguiente comando en Windows ```conda create -n guros Python ```
3.	Creado el entorno virtual se debe de inicializar con ```conda activate guros```
4.	Teniendo el entrono virtual activado en la carpeta de el repositorio se debe de usar el comando ```pip install -r requeriments.txt```
5.	Al tener instalados los requerimientos se debe de crear un archivo ```.env``` y añadir las siguientes variables con sus valores adaptados para el desarrollo local.
    ```DEBUG='True'
    DB_NAME='ToolderLocal'
    DB_USER='postgres'
    DB_PASSWORD='root'
    DB_PORT='5432'
    ALLOWED_HOST='127.0.0.1' ```
6.	Teniendo el entrono virtual en la carpeta de el proyecto se debe de hacer los siguientes comandos de django ```pyhton manage.py makemigrations, python manage.py migrate``` para crear las tablas de la base de datos
7.	Debes de crear tu usuario superuser con el comando ```python manage.py createsuperuser``` para generar tu usuario admin del sistema local


## Construido con 🛠️

* [Django](https://www.djangoproject.com/) - El framework web de python usado
* [PostgreSQL](https://www.postgresql.org/) - Gestor de bases de datos SQL

## Expresiones de Gratitud 🎁

* Comenta a otros sobre este proyecto 📢
* Da las gracias públicamente 🤓.
* Gracias por la oportunidad
