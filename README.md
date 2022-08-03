# Python-MongoDB-RestApi
 Creacion de ApiRestFull usando Flask framework, Docker y Mondodb Atlas
 
# Creacion de entorno Virtual

`virtualenv venv`

#### Iniciar entorno virtual
`.\venv\Scripts\activate`

# Crear imagen de contenedor
`docker build -t  [NombreContenedor] .`

#### Ejecutar el contenedor
`docker run -it --publish 5000:4000 [NombreContenedor]`

Ejecute el proyecto en el puerto local 5000 para aprovechar el proyecto de [FrontEnd](https://github.com/AldemarRamirez/FronEnd-Challenge) correspondiente.

# Servicios que se pueden consumir 
#### Metodo POST
1. http://localhost:5000/documento cargar un documento en la DB. Content-Type: application/json. Se recibe un JSON con las llaves titulo y contenido.
#### Metodo GET
1. http://localhost:5000/documento/?doc_name=320-8.txt realiza la busqueda del documento en la DB. Response JSON con el id, titulo y contenido.
2. http://localhost:5000/?doc_name=5985-8.txt&term=casa retorna la frecuencia del término en un documento especifico en la DB. Response JSON {'frecuencia': cantidad}
3. http://localhost:5000/?term=casa retorna la frecuencia del término en la coleccion de la DB. Response JSON {'frecuencia': cantidad}
