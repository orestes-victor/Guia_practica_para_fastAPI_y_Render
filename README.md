# Repositorio guia para fastAPI y RENDER
Este repositorio nace para facilitar el camino al usuario que necesita hacer funcionar su proyecto en fastAPI y en RENDER.

La explicación parte de tener preparado el archivo main.py con el codigo listo de las funciones para correr fastAPI, dichas funciones buscaran los datos en nuestros archivos parquet que se encuentran en la carpeta Dataset.

## Instalar el archivo `requirements.txt`

  Agrego el archivo requirements.txt:
  
  1. En la carpeta del proyecto en VisualStudio y en la consola de comando (terminal) pego lo siguiente:

  ```
  pip install -r requirements.txt
  ```

## Entorno virtual

Abro la consola de terminal

1. Instalo virtual env 

  ```
  pip install virtualenv
  ```

2. Creo un entorno virtual

  ```
  virtualenv nombre_del_entorno
  ```

3. Activo el entorno virtual

  ```
  nombre_del_entorno\Scripts\activate
  ```

4. Desactivo el entorno virtual

  ```
  deactivate
  ```



## FastAPI

1. Para correr el servidor de uvicorn, abro la consola de terminal y escribo
  ```
  uvicorn main:app --reload
  ```
2. Hago ***crtl+click*** en la dirección que te aparece en la terminal http://127.0.0.1:8000, luego agrego ya en el navegador agrego `/docs` y queda asi: http://127.0.0.1:8000/docs

3. Para terminar cierro el servidor uvicorn haciendo en la terminal ***crtl+C***
