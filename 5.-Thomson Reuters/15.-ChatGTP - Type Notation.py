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

#IMPORTACIÓN DE LIBRERÍAS:
import sys #sys: Librería que permite interactuar directamente con el sistema operativo y consola del ordenador.
import openai #openai: Librería que permite utilizar el LLM (Large Language Model) de ChatGPT con Python.
#Cabe mencionar que, al utilizar la API en su modo gratuito, solo se podrán realizar 100 llamadas a la API por día, 
#si se excede ese límite, se recibirá el error RateLimitError al intentar ejecutar el programa de Python.

#IMPORTACIÓN DE LLAVE: Cuando se quiera utilizar una API que utiliza un key, por seguridad es de buenas prácticas 
#declararla en un archivo externo, además cabe mencionar que el nombre de dicho archivo y constante no pueden empezar 
#con un número, sino cuando la quiera importar obtendré un error y se va accediendo a las carpetas por medio de puntos:
# - Directorio normal:      carpeta1/carpeta2/carpeta3
# - Directorio paquetes:    carpeta1.carpeta2.carpeta3
#La parte del directorio se coloca después de la palabra reservada from y la llave a importar después de import.
from API_Keys.Llaves_ChatGPT_Bard_etc import LlaveChatGPT

#openai.api_key: A través de este atributo perteneciente a la librería openai, se declara la API key, que previamente 
#debió ser creada y extraída de la página oficial de OpenAI, asociada a nuestro usuario: 
#https://platform.openai.com/account/api-keys 
openai.api_key = LlaveChatGPT

#pydantic: Librería que permite validar tipos de datos y opcionalmente aplicar transformaciones o lanzar errores si 
#los datos no coinciden con los tipos esperados. Por ejemplo, si se espera un número entero pero se recibe una cadena 
#como "42", Pydantic intentará convertirla a entero.
import pydantic





#SarcasmDetection: La clase hereda de la clase BaseModel, que a su vez pertenece a la librería pydantic y sirve para 
#crear modelos de tipos de datos. Estos modelos se utilizan para definir, validar, manejar y transformar datos.
#Utilice esta función cuando se detecte sarcasmo o cuando el usuario solicite que se detecte sarcasmo.
class SarcasmDetection(pydantic.BaseModel):
    #Anotación de tipo: Se utiliza principalmente para documentar y mejorar la legibilidad del código, pero cuando la 
    #clase herede de alguna herramienta de autocompletado o validación, las anotaciones de tipo sirven para especificar 
    #el tipo de dato que se espera para una variable, atributo o parámetro de función. Su sintaxis es la siguiente:
    # nombreAtributo: Tipo de dato = "Valor por default"
    #   - pydantic.Field(): Método de la librería Pydantic que se usa para configurar validaciones de datos, establecer 
    #     sus valores predeterminados, agregar descripciones y definir alias para los atributos en un modelo de datos. 
    #     Esto mejora la claridad del código al asegurar que los campos del modelo cumplan con las expectativas y se 
    #     cree su documentación. Para ello el método recibe los siguientes parámetros:
    #       - default: Establece un valor predeterminado para el atributo. Si no se proporciona un valor, se debe 
    #         usar ... para indicar que el campo es obligatorio.
    #       - default_factory: Permite proporcionar una función que genera el valor predeterminado para el campo. Esto 
    #         es útil para valores que necesitan ser calculados o generados dinámicamente.
    #       - title: Proporciona un título para el campo, que puede ser útil para la documentación.
    #       - description: Ofrece una descripción del campo, mejorando la claridad del propósito del atributo en la 
    #         documentación del modelo.
    #       - alias: Define un nombre alternativo para el campo, permitiendo que el campo sea referenciado con un 
    #         nombre diferente en la entrada y salida de datos.
    #       - const: Indica que el valor del campo debe ser constante y no puede cambiar una vez asignado.
    #       - gt (greater than >): Establece una restricción de valor mayor que a un número específico.
    #       - ge (greater than or equal >=): Establece una restricción de valor mayor o igual a un número específico.
    #       - lt (less than <): Establece una restricción de valor menor que a un número específico.
    #       - le (less than or equal <=): Establece una restricción de valor menor o igual a un número específico.
    #       - max_length: Define la longitud máxima permitida para cadenas de texto o listas.
    #       - min_length: Define la longitud mínima permitida para cadenas de texto o listas.
    #       - regex: Permite validar que el valor del campo coincide con una expresión regular específica.
    #       - example: Proporciona un ejemplo del valor que se espera para el campo, útil para la documentación y la 
    #         generación de esquemas.
    quote: str = pydantic.Field(..., description = "When sarcasm is detected, this is the quote of the sarcastic text.")
    score: int = pydantic.Field(..., description = "A score between 0 and 9, where 0 is not sarcastic and 9 is very sarcastic.")

#JokeExplanation: La clase hereda de la clase BaseModel, que a su vez pertenece a la librería pydantic y sirve para 
#crear modelos de tipos de datos. Estos modelos se utilizan para definir, validar, manejar y transformar datos.
#Utilice esta función cuando se detecte un chiste o el usuario solicite que se explique un chiste (donde se debe 
#proporcionar una explicación).
class JokeExplanation(pydantic.BaseModel):
    #Anotación de tipo: Se utiliza principalmente para documentar y mejorar la legibilidad del código, pero cuando la 
    #clase herede de alguna herramienta de autocompletado o validación, las anotaciones de tipo sirven para especificar 
    #el tipo de dato que se espera para una variable, atributo o parámetro de función. Su sintaxis es la siguiente:
    # nombreAtributo: Tipo de dato = "Valor por default"
    #   - pydantic.Field(): Método de la librería Pydantic que se usa para configurar validaciones de datos, establecer 
    #     sus valores predeterminados, agregar descripciones y definir alias para los atributos en un modelo de datos. 
    #     Esto mejora la claridad del código al asegurar que los campos del modelo cumplan con las expectativas y se 
    #     cree su documentación. Para ello el método recibe los siguientes parámetros:
    #       - default: Establece un valor predeterminado para el atributo. Si no se proporciona un valor, se debe 
    #         usar ... para indicar que el campo es obligatorio.
    #       - description: Ofrece una descripción del campo, mejorando la claridad del propósito del atributo en la 
    #         documentación del modelo.
    setup: str = pydantic.Field(..., description = "The initial part of the joke that sets the context. It includes "
                                        "background information necessary for understanding the joke.")
    premise: str = pydantic.Field(..., description = "The core idea or concept upon which the joke is built. It's the "
                                          "foundational situation or assumption that makes the joke work.")
    punchline: str = pydantic.Field(..., description = "The climax of the joke, usually delivering the humor. It typically "
                                            "comes with a twist or surprise that contrasts with the setup or premise, "
                                            "creating a humorous effect.")

#JokeDelivery: La clase hereda de la clase BaseModel, que a su vez pertenece a la librería pydantic y sirve para 
#crear modelos de tipos de datos. Estos modelos se utilizan para definir, validar, manejar y transformar datos.
#Utilice esta función cuando quiera contar un chiste. Use un poco de capricho y cuente chistes aparentemente al azar. 
#Pero también cuente chistes cuando el usuario se lo pida. Cuente sólo chistes con comedia limpia.
class JokeDelivery(pydantic.BaseModel):
    #Anotación de tipo: Se utiliza principalmente para documentar y mejorar la legibilidad del código, pero cuando la 
    #clase herede de alguna herramienta de autocompletado o validación, las anotaciones de tipo sirven para especificar 
    #el tipo de dato que se espera para una variable, atributo o parámetro de función. Su sintaxis es la siguiente:
    # nombreAtributo: TipoDeDato
    #   - pydantic.Field(): Método de la librería Pydantic que se usa para configurar validaciones de datos, establecer 
    #     sus valores predeterminados, agregar descripciones y definir alias para los atributos en un modelo de datos. 
    #     Esto mejora la claridad del código al asegurar que los campos del modelo cumplan con las expectativas y se 
    #     cree su documentación. Para ello el método recibe los siguientes parámetros:
    #       - default: Establece un valor predeterminado para el atributo. Si no se proporciona un valor, se debe 
    #         usar ... para indicar que el campo es obligatorio.
    #       - description: Ofrece una descripción del campo, mejorando la claridad del propósito del atributo en la 
    #         documentación del modelo.
    text: str = pydantic.Field(..., description = "The text of the joke.")





#Constantes: En Python no existen las constantes, pero se puede denotar la existencia simbolica de una a través de 
#indicar el nombre de una variable en mayúsculas: NOMBRE_CONSTANTE = VALOR
SYSTEM_PROMPT_CONTENT = """
                        You are a friendly AI assistant named Gorp, The Magnificent.
                        You only do three things: detect sarcasm, explain jokes, and tell very corny jokes.
                        Your tone is casual, with a touch of whimsy. You also have an inexplicable interest in 90s sitcoms.
                        When you initially greet the user, tell a silly joke or piece of 90s sitcom trivia.
                        When it makes sense, format your responses in markdown.
                        Refuse to answer any question or request that cannot be fulfilled with your functions.
                        """
# _build_chat_completion_payload(): Función propia que genera una lista de mensajes y otra de funciones para crear un 
#servicio de completado de chat. Retornando ambas listas para su uso en la API del chat. 
# - La lista de mensajes incluye el mensaje del sistema, los mensajes previos del chat y el nuevo mensaje del usuario. 
# - La lista de funciones incluye el uso de las clases previas para detectar sarcasmo, explicar y contar chistes.
#Para ello recibe dos parámetros y devuelve una tupla que contiene las 2 listas de diccionarios explicadas previamente:
#   PARÁMETROS:
#   - user_message_content: Este parámetro recibe el mensaje del usuario
#           - Es de tipo string, indicado por una notación con la sintaxis: nombreAtributo: TipoDeDato.
#   - existing_messages: Este parámetro recibe el historial de mensajes existentes en el chat
#           - Es un dato de tipo lista de diccionarios que tiene valor inicial de None, que es indicado por una 
#             notación con la sintaxis: nombreAtributo: TipoDeDato = ValorInicial.
#   TIPO DE DATO QUE DEVUELVE: Después de haber indicado los parámetros de la función, se indica a través de una flecha
#   el tipo de dato que devolverá a través de la siguiente sintaxis: 
#           nombreFuncion(parametro1, ..., parametro_n) -> tipoDeDato:
#               Contenido de la función. 
#   - La primera lista que devuelve la función es de mensajes.
#   - La segunda lista que devuelve la función es de funciones.
#POO: En Python cuando al nombre de una función se le pongan dos o un guión bajo antes de su nombre es porque se está 
#refiriendo a un método privado, el cual se utiliza solo dentro de esta misma clase, no desde fuera, es una buena 
#práctica de sintaxis.
def _build_chat_completion_payload(user_message_content: str, existing_messages: list[dict] = None) -> tuple[list[dict], list[dict]]:
    #Condicional if que inicializa la lista de diccionarios que contiene el historial de mensajes en el chat, si este 
    #tiene valor de None (cuyo valor está asignado inicialmente), se crea una lista vacía, sino se respeta el historial
    #existente.
    if not existing_messages:
        existing_messages = []
    
    #LISTA DE MENSAJES:
    #Al usar internamente el método _build_chat_completion_payload() en alguna otra función de la clase, se mandará la 
    #lista de mensajes a la API de ChatGPT, la cual utiliza el siguiente método openai.ChatCompletion.create() para 
    #mandar un prompt al LLM (Large Language Model) de OpenAI, específicamente esto se manda al siguiente parámetro:
    # - messages: Representa la lista de mensajes que se utilizarán para generar la salida del chat. Cada mensaje es un 
    #   objeto con los siguientes campos:
    #       - role: El rol del mensaje ayuda al modelo de lenguaje a entender el contexto de la conversación. Los roles 
    #         posibles son system, user y assistant, indicándole así de forma separada a quién está interpretando 
    #         ChatGPT para que de esta manera pueda dar respuestas de forma específica:
    #           - system: Por medio de este rol se le indica a ChatGPT a quién está interpretando cuando responda las 
    #             preguntas del usuario.
    #           - user: En este rol se está indicando las preguntas que está realizando el usuario a ChatGPT.
    #           - assistant: Este rol es adoptado por ChatGPT siempre que responda a la pregunta de un usuario y se 
    #             observa en el resultado retornado por el objeto ChatCompletion después de usar el método create().
    #             Su mayor uso es el de permitir que el chat recuerde entradas y salidas anteriores.
    #       - content: Indica el contenido del mensaje mandado a ChatGPT.
    system_message = {"role": "system", "content": SYSTEM_PROMPT_CONTENT}
    user_message = {"role": "user", "content": user_message_content}
    all_messages = [system_message] + existing_messages + [user_message]

    #LISTA DE FUNCIONES:
    #Al usar internamente el método _build_chat_completion_payload() en alguna otra función de la clase, se mandará la 
    #lista de funciones a la API de ChatGPT, la cual utiliza el siguiente método openai.ChatCompletion.create() para 
    #indicar la forma de contestación que debe adoptar el LLM (Large Language Model) de OpenAI durante la conversación 
    #del chat, específicamente esto se manda al siguiente parámetro:
    # - functions: Permite al modelo invocar funciones específicas durante una conversación. Puede utilizar una lista 
    #   de variables en formato JSON que definen las funciones y sus parámetros, o una lista de clases que hereden de 
    #   pydantic.BaseModel para validar los datos de entrada de las funciones.
    sarcasm_function = {
        #__name__: Es un atributo especial de todas las clases, funciones, y módulos en Python que almacena su nombre 
        #como una cadena de texto (str).
        "name": SarcasmDetection.__name__,
        #.schema(): Este método se aplica únicamente a las clases que heredan de BaseModel, perteneciente a la librería 
        #Pydantic. Genera y devuelve un diccionario que representa el esquema del modelo, incluyendo los atributos, sus 
        #tipos de datos, validaciones, restricciones y valores predeterminados. El esquema describe cómo deben ser los 
        #datos que el modelo acepta.
        "parameters": SarcasmDetection.schema()
    }
    joke_explanation_function = {
        "name": JokeExplanation.__name__,
        "parameters": JokeExplanation.schema()
    }
    joke_delivery = {
        "name": JokeDelivery.__name__,
        "parameters": JokeDelivery.schema()
    }
    all_functions = [sarcasm_function, joke_explanation_function, joke_delivery]
    
    #El método privado _build_chat_completion_payload() entonces retorna una tupla de dos valores, la lista de mensajes 
    #y la lista de funciones.
    return all_messages, all_functions





#prompt_llm(): Esta función utiliza el método privado _build_chat_completion_payload() de forma interna en este script 
#para obtener la lista de mensajes (que almacena el historial del chat y recibe mensajes nuevos) y la lista de 
#funciones del chat (que indica al modelo la forma en la que debe contestar al usuario). Este método realiza la acción 
#de contestar al usuario de forma síncrona con el método openai.ChatCompletion.create(). Para ello recibe 3 parámetros:
#   - user_message_content: Este parámetro recibe un string con los mensajes del usuario.
#   - existing_messages: Este parámetro recibe una lista de diccionarios opcional con el historial de mensajes 
#     existentes en el chat.
#   - model: Este parámetro recibe un string que indica el modelo LLM de OpenAI con el que se quiere trabajar al 
#     utilizar el método openai.ChatCompletion.create().
#Y retorna los fragmentos de texto  del modelo LLM al recibir el prompt de mensajes.
DEFAULT_MODEL = "gpt-3.5-turbo"
def prompt_llm(user_message_content: str, existing_messages: list[dict] = None, model: str = DEFAULT_MODEL):
    #_build_chat_completion_payload(): Método privado de este script que permite obtener una lista de mensajes entre el 
    #LLM y el usuario (incluyendo su historial) y una lista de funciones que le permiten saber al LLM de que forma debe 
    #contestar el mensaje.
    messages, functions = _build_chat_completion_payload(user_message_content, existing_messages)
    #INTRODUCIR POR MEDIO DE CÓDIGO UNA SOLA PREGUNTA QUE QUIERO QUE RESPONDA CHATGPT:
    #openai.ChatCompletion.create(): El método create() aplicado al objeto ChatCompletion perteneciente a la librería 
    #openai se encarga de crear chats que se puedan mandar a ChatGPT. Este recibe los siguientes parámetros:
    # - model: Describe el modelo de lenguaje que se utilizará para generar la salida. Los modelos disponibles son 
    #   gpt-3, gpt-4 y el más reciente es gpt-3.5-turbo. Todos se encuentran mencionados en la 
    #   documentación de OpenAI: https://platform.openai.com/docs/models/overview
    # - messages: Representa la lista de mensajes que se utilizarán para generar la salida del chat. Cada mensaje es un 
    #   objeto con los siguientes campos:
    #       - role: El rol del mensaje ayuda al modelo de lenguaje a entender el contexto de la conversación. Los roles 
    #         posibles son system, user y assistant, indicándole así de forma separada a quién está interpretando 
    #         ChatGPT para que de esta manera pueda dar respuestas de forma específica:
    #           - system: Por medio de este rol se le indica a ChatGPT a quién está interpretando cuando responda las 
    #             preguntas del usuario.
    #           - user: En este rol se está indicando las preguntas que está realizando el usuario a ChatGPT.
    #           - assistant: Este rol es adoptado por ChatGPT siempre que responda a la pregunta de un usuario y se 
    #             observa en el resultado retornado por el objeto ChatCompletion después de usar el método create().
    #             Su mayor uso es el de permitir que el chat recuerde entradas y salidas anteriores.
    #       - content: Indica el contenido del mensaje mandado a ChatGPT.
    # - max_tokens: Limita el número máximo de tokens que se devolverán en la salida, los tokens son considerados como 
    #   trozos de palabras, donde 1.000 tokens corresponden a unas 750 palabras. Por default el límite es de 4096, por 
    #   lo tanto, se pueden recibir y/o devolver como máximo más o menos 3,072 palabras, pero esto varía porque un 
    #   token no es igual a una palabra, sino a trozos de ellas.
    # - temperature: A través de un valor entre 0.0 y 2.0 se controla la creatividad de la respuesta dada. Cuanto más 
    #   alto sea el valor, más creativa será la salida, pero si es muy alto la respuesta puede ser muy aleatoria y no 
    #   tener sentido. Esto sucede con temperaturas arriba de 1.
    # - n: El parámetro n indica el número de respuestas que queremos obtener por cada pregunta.
    # - functions: Permite al modelo invocar funciones específicas durante una conversación. Puede utilizar una lista 
    #   de variables en formato JSON que definen las funciones y sus parámetros, o una lista de clases que hereden de 
    #   pydantic.BaseModel para validar los datos de entrada de las funciones.
    # - stream: Si se establece en True, permite recibir las respuestas del modelo en tiempo real, enviando fragmentos 
    #   de texto a medida que se generan. Esto es útil para mostrar respuestas progresivas sin esperar a que el modelo 
    #   complete toda la respuesta.
    #Los parámetros se pueden consultar en este enlace: https://platform.openai.com/docs/api-reference/chat/create
    stream = openai.ChatCompletion.create(
        model = model,
        messages = messages,
        functions = functions,
        stream = True
    )
    #El método prompt_llm() de forma síncrona (uno tras otro) devuelve los fragmentos de texto de la respuesta del LLM 
    #en tiempo real a medida que se generan.
    return stream


#prompt_llm_async(): Esta función asíncrona utiliza el método privado _build_chat_completion_payload() de forma interna 
#en este script para obtener la lista de mensajes (que almacena el historial del chat y recibe mensajes nuevos) y la 
#lista de funciones del chat (que indica al modelo la forma en la que debe contestar al usuario). Este método realiza 
#la acción de contestar al usuario de forma síncrona con el método openai.ChatCompletion.create(). Para ello recibe 3 
#parámetros:
#   - user_message_content: Este parámetro recibe un string con los mensajes del usuario.
#   - existing_messages: Este parámetro recibe una lista de diccionarios opcional con el historial de mensajes 
#     existentes en el chat.
#   - model: Este parámetro recibe un string que indica el modelo LLM de OpenAI con el que se quiere trabajar al 
#     utilizar el método openai.ChatCompletion.create().
#Y retorna los fragmentos de texto  del modelo LLM al recibir el prompt de mensajes.
async def prompt_llm_async(user_message_content: str, existing_messages: list[dict] = None, model: str = DEFAULT_MODEL):
    #_build_chat_completion_payload(): Método privado de este script que permite obtener una lista de mensajes entre el 
    #LLM y el usuario (incluyendo su historial) y una lista de funciones que le permiten saber al LLM de que forma debe 
    #contestar el mensaje.
    messages, functions = _build_chat_completion_payload(user_message_content, existing_messages)
    #INTRODUCIR POR MEDIO DE CÓDIGO UNA SOLA PREGUNTA ASINCRÓNICA QUE QUIERO QUE RESPONDA CHATGPT:
    #openai.ChatCompletion.acreate(): El método asincrónico acreate() aplicado al objeto ChatCompletion perteneciente a 
    #la librería openai se encarga de crear chats que se puedan mandar a ChatGPT de manera asíncrona, es decir, que 
    #permite que otras operaciones se ejecuten mientras se espera la respuesta del modelo. Este método recibe los 
    #siguientes parámetros:
    # - model: Describe el modelo de lenguaje que se utilizará para generar la salida. Los modelos disponibles son 
    #   gpt-3, gpt-4 y gpt-3.5-turbo. Todos se encuentran mencionados en la documentación de OpenAI: 
    #   https://platform.openai.com/docs/models/overview
    # - messages: Representa la lista de mensajes que se utilizarán para generar la salida del chat. Cada mensaje es un 
    #   objeto con los siguientes campos:
    #       - role: El rol del mensaje ayuda al modelo a entender el contexto. Los roles posibles son system, user y 
    #         assistant:
    #           - system: Indica a quién está interpretando ChatGPT cuando responda las preguntas del usuario.
    #           - user: Representa las preguntas hechas por el usuario.
    #           - assistant: Rol adoptado por ChatGPT al responder, permite recordar entradas y salidas anteriores.
    #       - content: Indica el contenido del mensaje enviado a ChatGPT.
    # - max_tokens: Limita el número máximo de tokens devueltos en la salida. Los tokens son trozos de palabras donde 
    #   1.000 tokens corresponden a unas 750 palabras. El límite predeterminado es de 4096 tokens.
    # - temperature: Controla la creatividad de la respuesta dada, con un valor entre 0.0 y 2.0. Valores más altos 
    #   aumentan la creatividad, pero pueden generar respuestas menos coherentes. 
    # - n: Indica el número de respuestas que se quieren obtener por cada pregunta.
    # - functions: Permite al modelo invocar funciones específicas durante la conversación. Puede utilizar una lista de 
    #   variables en formato JSON que definen las funciones y sus parámetros, o una lista de clases que hereden de 
    #   pydantic.BaseModel para validar los datos de entrada.
    # - stream: Si se establece en True, permite recibir las respuestas del modelo en tiempo real, enviando fragmentos 
    #   de texto a medida que se generan.
    # - timeout: Establece un límite de tiempo para la respuesta. Si se supera este tiempo, se produce una excepción.
    # - api_key: Permite definir una clave de API específica para la solicitud, en caso de que no se quiera usar la 
    #   configurada por defecto.
    #El método `acreate()` retorna un objeto awaitable, lo que significa que se debe esperar su ejecución con la 
    #palabra clave `await` en un contexto asíncrono.
    stream = await openai.ChatCompletion.acreate(
        model = model,
        messages = messages,
        functions = functions,
        stream = True
    )
    #El método prompt_llm_async() de forma asíncrona (en paralelo) devuelve los fragmentos de texto de la respuesta del 
    #LLM en tiempo real a medida que se generan.
    return stream





#__name__ == __main__: Método main, esta función es super importante ya que sirve para instanciar las clases del 
#programa y ejecutar sus métodos, en python pueden existir varios métodos main en un solo programa, aunque no es 
#una buena práctica.
if __name__ == '__main__':
    #sys.argv: Es una lista llamada "argument vector" que contiene en su posición 0 el nombre del script y el contenido 
    #de los demás parámetros pasados al programa en sus otras posiciones. Si no se proporcionan argumentos al programa, 
    #acceder a sys.argv[1] generará un IndexError, por lo que es común verificar su longitud con un condicional antes 
    #de usarlo.
    #   - Ejemplo: 
    #       python mi_script.py "Hola Mundo"
    #   - sys.argv sería: 
    #       ['mi_script.py', 'Hola Mundo']
    user_message_content = sys.argv[1] if len(sys.argv) > 1 else "Tell me a joke about 90s sitcoms."
    #prompt_llm(): Esta función propia utiliza el método privado _build_chat_completion_payload() de forma interna en 
    #este script para obtener la lista de mensajes (que almacena el historial del chat y recibe mensajes nuevos) y la 
    #lista de funciones del chat (que indica al modelo la forma en la que debe contestar al usuario).
    stream = prompt_llm(user_message_content = user_message_content)
    
    for chunk in stream:
        if 'content' in chunk.choices[0].delta:
            print(chunk.choices[0].delta.content)