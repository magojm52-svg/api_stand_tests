# Importa el archivo 'configuration.py' (asumiendo que ese es el nombre del archivo de configuración)
# Esto nos permitirá acceder a variables como URL_SERVICE y DOC_PATH
import configuration

# Importa la librería 'requests' para realizar solicitudes HTTP
import requests

#importando el contenido de un archivo de Python llamado data.py
#a tu archivo actual (sender_stand_request.py y luego usar sus datos)
import data

#define una función llamada get_docs
# Cuando se llama a esta función, realiza una solicitud GET a la combinación de URL_SERVICE y DOC_PATH
#(es decir, la URL completa de la documentación).
def get_docs():
    #Devuelve el resultado de enviar una solicitud HTTP de tipo GET a la dirección web que
    #resulta de unir la URL del servicio base con la ruta específica de la documentación
    return requests.get(configuration.URL_SERVICE + configuration.DOC_PATH)

#solicitud GET a la URL de los logs construida a partir de tu configuration
def get_logs():
    # params: Le dice a la librería requests que los datos proporcionados filtrando los 20  mas recientes
    return requests.get(configuration.URL_SERVICE + configuration.LOG_MAIN_PATH, params={"count": 20})


def get_users_table():
    return requests.get(configuration.URL_SERVICE + configuration.USERS_TABLE_PATH)

def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,  # inserta la dirección URL completa
                         json=body,  # inserta el cuerpo de solicitud
                         headers=data.headers)  # inserta los encabezados

def post_products_kits(products_ids):
    # Realiza una solicitud POST para buscar kits por productos.
    return requests.post(configuration.URL_SERVICE + configuration.PRODUCTS_KITS_PATH, # Concatenación de URL base y ruta.
                         json=products_ids, # Datos a enviar en la solicitud.
                         headers=data.headers) # Encabezados de solicitud.
