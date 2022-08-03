# Python-MongoDB-RestApi
 Creacion de ApiRestFull usando Flask framework, Docker y Mondodb Atlas

Creacion de entorno virtual
virtualenv venv

Iniciar entorno virtual
.\venv\Scripts\activate

Crear imagen 
docker build -t  [NombreContenedor] .

Ejecutar el contenedor en el puerto local 5000
Por defecto se ejecuta en el puerto 4000 en el contenedor
Se recomienda ejecutar en el puerto 5000 local para usar el proyecto FrontEnd
docker run -it --publish 5000:4000 [NombreContenedor]
