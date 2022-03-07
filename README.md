#### Prueba técnica ASD

- Descargar base de datos backupASD
- Importar la base de datos PostgreSQL 
- clonar el repositorio -> https://github.com/Danielmc09/pruebaASD.git
- crear un entorno virtual  -> virtualenv name_env
- activar entorno virtual 
- instalar librerias  ->  (env) pip install -r requirements.txt 
- ejecutar el proyecto
- cambiar la configuración de la base de datos en el archivo settings.py 
- Importar la collection en POSTMAN para realizar las pruebas
- Para el create encuentra un ejemplo en la apartado del body
- Para el update encuentra un ejemplo en la apartado del body

- Puertos a utilizar que no deben estar ocupados o con los servicios locales apagados:
  - Django: 8000
  - Postgresql: 5432

- Endpoints:

|Path|Verb
|----|----
|http://127.0.0.1:8000/areas/|GET
|http://127.0.0.1:8000/personas/|GET
|http://127.0.0.1:8000/activos/|GET
|http://127.0.0.1:8000/activos/activostipo/|GET
|http://127.0.0.1:8000/activos/activosfechacompra/|GET
|http://127.0.0.1:8000/activos/activosserial/|GET
|http://127.0.0.1:8000/activos/activoscreate/|POST
|http://127.0.0.1:8000/activos/activosupdate/<int:pk>|PUT

- parametros para el endpoint /activos/activostipo/ -> tipo_activo
- parametros para el endpoint /activos/activosfechacompra/ -> fecha_compra
- parametros para el endpoint /activos/activosserial/ -> serial
- parametros para el endpoint /activos/activosupdate/<int:pk> -> id


Autor: Angel Daniel Menideta Castillo © 2021
