# API de releases

Este repositorio contiene el código fuente del proyecto API de releases.
Dicho proyecto es una API REST que permite la gestión de releases de software y sus usuarios, el mismo fue desarrollado con:
- Python 3.12.2
- Django 5.0.4
- Django Rest Framework 3.15.1
  
El API esta formada por las aplicaciones `releases` y `users`, las cuales contienen los models, serializers, vistas y urls necesarias para la gestión de releases y usuarios respectivamente.

## Instalación
1. Clonar el repositorio
2. Crear un entorno virtual con Python 3.12.2
3. Instalar las dependencias con `pip install -r requirements.txt`
4. Crear la base de datos con `python manage.py migrate`
5. Correr el servidor con `python manage.py runserver`
6. Acceder a la API en `http://localhost:8000/`
   
## Endpoints
### Users
- `POST /users/login`: Permite loguear un usuario con su email y contraseña.
- `POST /users/register`: Permite registrar un nuevo usuario con su username, email y contraseña (opcional: first_name, last_name).
- `GET /users/profile`: Permite obtener el perfil del usuario autenticado.
- `GET /users/:id/releases`: Permite obtener los releases del usuario con el id especificado.
- `POST /users/logout`: Permite desloguear al usuario autenticado.

### Releases
- `GET /releases`: Permite obtener todos los releases.
- `GET /releases/:id`: Permite obtener un release con el id especificado.
- `POST /releases/create`: Permite crear un nuevo release con su title, description, tag y version (el author se coloca el del usuario logueado, el created_at es automatico).
- `PATCH /releases/update/:id`: Permite actualizar un release con el id especificado.
- `DELETE /releases/delete/:id`: Permite eliminar un release con el id especificado.

### Aclaraciones
Los endpoints de los releases (excepto los GET) se encuentran protegidos, es decir que solo pueden ser accedidos por usuarios autenticados.
El usuario autenticado se obtiene a través del token que se envía en el header de la petición.
El método POST puede realizarlo cualquier usuario logueado, pero el PATCH y DELETE solo pueden ser realizados por el autor del release (estando logueado).

En cuanto a los endpoints de los usuarios, el login y register no requieren autenticación, pero el profile y logout si.

## Consultas a endpoints
En caso de querer realizar consultas a la API desplegada en [Render](https://render.com/) en lugar de usar la ruta local se debe usar la siguiente URL: **https://releases-backend.onrender.com/**

## Consultas con insomnia
Si se tiene instalado el software de [insomnia](https://insomnia.rest/), se puede ahorrar pasos para realizar las consultas a la API desplegada importando las colecciones [releases](./releases_collection.json) y [users](./users_collection.json).
Las mismas contienen las consultas a los endpoints de releases y users respectivamente. 