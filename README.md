# Gurus test

## Comenzando 🚀
Este repositorio es para albergar el backend de el test de "Requerimos que desarrolles un proyecto que detecte si una persona tiene diferencias genéticas basándose en
su secuencia de ADN"

### Pre-requisitos 📋

_Tener instalado Python y Conda_


### Instalación 🔧

1.	Clonar el repositorio.
2.	Se debe de crear un entorno virtual de conda dentro de la carpeta del repo, de sugerencia se debe de llamar guros esto se hace con el siguiente comando en Windows ```conda create -n guros Python ```
3.	Creado el entorno virtual se debe de inicializar con ```conda activate guros```
4.	Teniendo el entrono virtual activado en la carpeta de el repositorio se debe de usar el comando ```pip install -r requeriments.txt```
5.	Teniendo el entrono virtual en la carpeta de el proyecto se debe de hacer los siguientes comandos de django ```pyhton manage.py makemigrations, python manage.py migrate``` para crear las tablas de la base de datos
6.	Debes de crear tu usuario superuser con el comando ```python manage.py createsuperuser``` para generar tu usuario admin del sistema local
7. Al tener el usuario el siguiente paso es correr el comand ```python manage.py runserver``` para arrancar el servidor en localhost:3000
8. Para revisar las rutas definidas sobre el test serián _GET http://localhost:8000/dna/stats_ y _POST http://localhost:8000/dna/mutation_
9. El objeto que se debe de mandar en el post debe de tener la siguiente estructura: ```{
    "dna":["AATAAT", "CAGGGC", "TAGTGT", "TGGGTG", "CGCCTA","TCACTG" ]
}``` en caso contrario marcara error el sistema
10. Para la petición GET solo es acceder a la ruta


## Construido con 🛠️

* [Django](https://www.djangoproject.com/) - El framework web de python usado

## Expresiones de Gratitud 🎁

* Comenta a otros sobre este proyecto 📢
* Da las gracias públicamente 🤓.
* Gracias por la oportunidad
