# DBII - RestAPI Project 

## Ejecutar Proyecto:
### Pre-requisitos:
Tener instalado:

- Git

- Python

- Visual Studio Code (VSC) o Spider


### Dependencias:

- Clonar Repositorio `git clone https://github.com/DataBaseII/project-api.git`

- Abrir con  VSC el folder `project-api`

- Abrir una terminal

- Ejecutar `pip install virtualenv`

- Ejecutar `virtualenv venv`

- Ejecutar `.\venv\Scripts\activate.bat`

- Ejecutar `pip install flask pymongo`

- Ejecutar `pip install flask-pymongo`

- Ejecutar `pip install -U flask-cors`

### Levantar Server:

- Ejecutar `python src/app.py`

### El Servidor se levantara en el puerto `http://localhost:5000/api/v1`

### Funcionalidades

#### Movies

- **[Metodo : GET]** - Obtener todas las peliculas `http://localhost:5000/api/v1/movies`

- **[Metodo : GET]** - Obtener una pelicula por ID `http://localhost:5000/api/v1/movies/<id>`

- **[Metodo : POST]** - Crear una pelicula `http://localhost:5000/api/v1/movies`

- **[Metodo : PUT]** - Actualizar una pelicula `http://localhost:5000/api/v1/movies/<id>`

- **[Metodo : DELETE]** - Eliminar una pelicula `http://localhost:5000/api/v1/movies/<id>`

#### Users

- **[Metodo : GET]** - Obtener todos los usuarios `http://localhost:5000/api/v1/users`

- **[Metodo : GET]** - Obtener un usuario por ID `http://localhost:5000/api/v1/users/<id>`

- **[Metodo : POST]** - Crear un usuario `http://localhost:5000/api/v1/users`

- **[Metodo : PUT]** - Actualizar un usuario `http://localhost:5000/api/v1/users/<id>`

- **[Metodo : DELETE]** - Eliminar un usuario `http://localhost:5000/api/v1/users/<id>`

#### Genres

- **[Metodo : GET]** - Obtener todas las categorias `http://localhost:5000/api/v1/categories`

- **[Metodo : GET]** - Obtener una categoria por ID `http://localhost:5000/api/v1/categories/<id>`

- **[Metodo : POST]** - Crear una categoria `http://localhost:5000/api/v1/categories`

- **[Metodo : PUT]** - Actualizar una categoria `http://localhost:5000/api/v1/categories/<id>`

- **[Metodo : DELETE]** - Eliminar una categoria `http://localhost:5000/api/v1/categories/<id>`

## Explicacion

En el archivo `app.py` estan las rutas habilitadas

Dentro del folder `services` tenemos los servicios para categorias, usuarios y peliculas.

Dentro del folder `utils` estan 2 archivos comunes que se utilizan en el proyecto.

### Colecciones

En `user` tenemos los datos para que un usuario pueda hacer login.

```json
user:{
  "username": "Adrian",
  "email": "adrian@correo.com",
  "password": "adrian123",
  "isAdmin": false
}
```

En `movie` tenemos los datos para una movie, genreId nos ayuda a conectar con la coleccion de genres, idioms y actors son arreglos.

```json
movie: {
	"name": "Taxi driver",
	"year": "1976",
	"imageBG": "https://www.teahub.io/photos/full/188-1889115_taxi-driver-movie-scenes.jpg", 
	"imageCard":"https://m.media-amazon.com/images/M/MV5BM2M1MmVhNDgtNmI0YS00ZDNmLTkyNjctNTJiYTQ2N2NmYzc2XkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_.jpg",
	"video": "T5IligQP7Fo", 
	"duration": "1:52",
	"genreId": category.key,
	"sinopsis": "Para sobrellevar el insomnio crónico que sufre desde su regreso de Vietnam, Travis Bickle trabaja como taxista nocturno en Nueva York.",
	"director": "Martin Scorsese", 
	"idioms": ["Ingles", "Español"],
	"actors": ["Robert De Niro", "Jodie Foster", "Albert Brooks", "Harvey Keitel", "Peter Boyle", "Cybill Shepherd"]
}
```
En `category` tenemos los datos para una categoria, el field key nos ayuda a conectar con la movie con una categoria.

```json
category: {
  "key":"2",
  "value":"Ficcion"
}
```


## Dependencies:

```
pip install virtualenv

virtualenv venv

.\venv\Scripts\activate.bat 

pip install flask pymongo 

pip install flask-pymongo

pip install black

pip install -U flask-cors

black src

python src/app.py
```
### Developed by:

- Adrian Mendoza

- Jhulians Garcia

- Jose Carlos Lopez