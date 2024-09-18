# -*- coding: utf-8 -*-

#En Python se introducen comentarios de una sola linea con el simbolo #.
#La primera línea de código incluida en este programa se conoce como declaración de codificación o codificación 
#de caracteres. Al especificar utf-8 (caracteres Unicode) como la codificación, nos aseguramos de que el archivo 
#pueda contener caracteres especiales, letras acentuadas y otros caracteres no ASCII sin problemas, garantizando 
#que Python interprete correctamente esos caracteres y evite posibles errores de codificación.
#Se puede detener una ejecución con el comando [CTRL] + C puesto en consola, con el comando "cls" se borra su 
#historial y en Visual Studio Code con el botón superior derecho de Play se corre el programa.
#Para comentar en Visual Studio Code varias líneas de código se debe pulsar:
#[CTRL] + K (VSCode queda a la espera). Después pulsa [CTRL] + C para comentar y [CTRL] + U para descomentar.

#IMPORTACIÓN DE CLASES: Cuando se quiera importar una clase, el nombre de esta no puede empezar con un número, 
#sino cuando la quiera importar obtendré un error y se va accediendo a las carpetas o también llamados paquetes 
#en la programación orientada a objetos (POO), por medio de puntos:
# - Directorio normal:      carpeta1/carpeta2/carpeta3
# - Directorio paquetes:    carpeta1.carpeta2.carpeta3
#La parte del directorio se coloca después de la palabra reservada from y la clase a importar después de import.
from POO_API_AsistenteVirtual import ChatGPT_TypeNotation

#IMPORTACIÓN DE LLAVE: Cuando se quiera utilizar una API que utiliza un key, por seguridad es de buenas prácticas 
#declararla en un archivo externo, además cabe mencionar que el nombre de dicho archivo y constante no pueden empezar 
#con un número, sino cuando la quiera importar obtendré un error y se va accediendo a las carpetas por medio de puntos:
# - Directorio normal:      carpeta1/carpeta2/carpeta3
# - Directorio paquetes:    carpeta1.carpeta2.carpeta3
#La parte del directorio se coloca después de la palabra reservada from y la llave a importar después de import.
from API_Keys.Llaves_ChatGPT_Bard_etc import LlaveChatGPT

#IMPORTACIÓN DE LIBRERÍAS:
#AsyncIO: Librería que permite escribir código concurrente (asíncrono) que puede realizar múltiples tareas al mismo 
#tiempo sin la necesidad de usar hilos (threads) o procesos múltiples. En lugar de bloquear el programa mientras se 
#espera una operación de I/O (entradas/salidas como leer de una base de datos, recibir datos de una API o interactuar 
#con un archivo), asyncio permite que otras tareas continúen ejecutándose.
import asyncio
#random: Librería para generar números aleatorios y realizar operaciones relacionadas con la aleatoriedad.
import random

#FastAPI: Es una bilbioteca para crear APIs web rápidas y eficientes. Está basada en la librería Starlette para la 
#gestión de solicitudes HTTP y la librería Pydantic para la validación de datos, lo que la convierte en una opción 
#ideal para construir APIs modernas y robustas. Sus mayores ventajas son:
# - Documentación Automática: Mientras se construyan los endpoints de la API (las carpetas o rutas de la URL) usando 
#   los 4 métodos HTTP que conforman el CRUD (Create, Read, Update y Delete): GET, POST, PUT y DELETE. Se estará 
#   creando automáticamente una documentación de su uso al acceder al endpoint URL/docs.
#       - Create -> POST: Método HTTP que permite mandar datos al endpoint de una API.
#       - Read ->   GET: Método HTTP que permite obtener los datos almacenados en algún endpoint de una API.
#       - Update -> PUT: Método HTTP que permite actualizar los datos previamente almacenados en un endpoint.
#       - Delete -> DELETE: Método HTTP que permite borrar los datos previamente almacenados en un endpoint.
# - Validación de Datos: Estos se realizan a través de la librería Pydantic, la cual realiza operaciones de anotación 
#   de datos con la siguiente sintaxis: nombreAtributo: Tipo de dato = "Valor por default".
#Para crear las conexiones con FastAPI se tienen que realizar las siguientes instalaciones:
#pip install fastapi: La API que permite utilizar el servidor de Uvicorn.
#pip install uvicorn: Uvicorn es un servidor ASGI (Asynchronous Server Gateway Interface) y es un estándar para la 
#interfaz entre servidores web y aplicaciones web en Python, permitiendo así manejar solicitudes asíncronas de manera 
#eficiente. Está diseñado para ser compatible con aplicaciones web modernas que requieren manejo de operaciones 
#asíncronas, como websockets y aplicaciones en tiempo real.
#Para levantar el servidor de FastAPI se debe utilizar el siguiente comando en consola:
#   uvicorn nombreArchivoPython:nombreInstanciaFastAPI --reload
import fastapi
#sse_starlette: Esta librería se utiliza en aplicaciones web que usen la bilbioteca FastAPI para habilitar el soporte 
#de Server-Sent Events (SSE); tecnología que permite al servidor enviar actualizaciones automáticas al cliente a través 
#de una conexión HTTP persistente, lo que facilita la transmisión continua de datos en tiempo real.
import sse_starlette

#fastapi.FastAPI(): Con esto se crea una instancia de la librería FastAPI para poder crear las rutas (endpoints) de una 
#API y así manejar las diferentes solicitudes HTTP específicas que conforman el CRUD: Create, Read, Update y Delete.
#Esta instancia se utiliza en el siguiente comando de consola que sirve para levantar el servidor:
#   uvicorn nombreArchivoPython:nombreInstanciaFastAPI --reload
#       - uvicorn: Es el servidor de tipo ASGI que utiliza la librería FastAPI.
#       - nombreArchivoPython: Es el nombre de este archivo Python, el cual no puede empezar con un número y no puede 
#         contener caracteres especiales más que el guión bajo.
#       - nombreInstanciaFastAPI: Es el nombre de la instancia de FastAPI dentro de este archivo Python.
#       - Comandos de configuración de servidor, estos son algunos de ellos:
#           --host: Especifica la dirección IP en la que el servidor escuchará. Por defecto es 127.0.0.1.
#           --port: Define el puerto en el que el servidor escuchará. Por defecto es 8000.
#           --reload: Habilita la recarga automática del servidor cuando detecta cambios en el código. Ideal para 
#           desarrollo.
#           --workers: Número de procesos de trabajo a usar. Aumentar el número de trabajadores puede mejorar el 
#           rendimiento en producción. 
#Para ver el resultado de la API, debemos acceder al siguiente URL a través de nuestro navegador: http://127.0.0.1:8000
#Sobre este URL es que se podrá ver el resultado de los diferentes endpoints de la API: http://127.0.0.1:8000/EndPoints
app = fastapi.FastAPI()

#Métodos HTTP: Sobre la instancia de FastAPI que ha levantado el servidor Uvicorn se pueden ejecutar funciones propias 
#síncronas y asíncronas que apliquen los siguientes métodos HTTP sobre los distintos endpoints creados en esta URL: 
#http://127.0.0.1:8000/EndPoints
#Los métodos HTTP de la API creada con la librería FastAPI crearán una documentación automática al utilizarse: 
# - Documentación Automática: Mientras se construyan los endpoints de la API (las carpetas o rutas de la URL) usando 
#   los 4 métodos HTTP que conforman el CRUD (Create, Read, Update y Delete): GET, POST, PUT y DELETE. Se estará 
#   creando automáticamente una documentación de su uso al acceder al endpoint URL/docs.
#       - Create -> POST: Método HTTP que permite mandar datos al endpoint de una API.
#       - Read ->   GET: Método HTTP que permite obtener los datos almacenados en algún endpoint de una API.
#       - Update -> PUT: Método HTTP que permite actualizar los datos previamente almacenados en un endpoint.
#       - Delete -> DELETE: Método HTTP que permite borrar los datos previamente almacenados en un endpoint.
#@: Esto se llama decorador y su función es la de tomar un método y agregarle una funcionalidad extra. En específico la 
#función del decorador al utilizarse junto la instancia de FastAPI es la de indicarle al programa la acción a ejecutar 
#al acceder a cierto endpoint.
@app.get("/stream-example")
#stream_example(): Función asíncrona propia que sirve para transmitir texto en un chat donde se lleva una conversación 
#entre usuario y un asistente virtual de ChatGPT, en particular transmitiendo texto del servidor al cliente mandando 
#una palabra o token a la vez. 
async def stream_example():
    #stream_tokens(): Implementación de marcador de posición para la transmisión de tokens. Pruebe a ejecutar esta ruta 
    #tal cual para comprender mejor cómo transmitir datos mediante eventos enviados por el servidor (SSE) en FastAPI.
    #Para más información checar: https://devdojo.com/bobbyiliev/how-to-use-server-sent-events-sse-with-fastapi
    async def stream_tokens():
        for token in ['hello', ', ', 'this ', 'is ', 'a ', 'streamed ', 'response.']:
            # fake delay: 
            await asyncio.sleep(random.randint(0, 3))
            print(f"Yielding token: {token}")
            yield token
    return sse_starlette.sse.EventSourceResponse(stream_tokens())
# Your code/routes here (you may also keep code in separate files and import/it them here):