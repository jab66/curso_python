import requests
from dotenv import load_dotenv
import os

load_dotenv()
url = os.getenv("api_url")
print(url)

# recuperar todos los elementos de la api
# respuesta = requests.get(url, timeout=10)
# print(respuesta.status_code)
# print(respuesta.text)
# respuesta = respuesta.json()
# for user in respuesta:
#     print(user["name"])

# buscar un usuario
# id = 1
# url_user = os.getenv("api_url")
# url_user = url_user+f"/{id}"

# print(url_user)

# respuesta = requests.get(url_user, timeout=10)
# respuesta = respuesta.json()
# print(respuesta)
# print(respuesta["name"])
# print(respuesta["address"]["street"])

# hacer un POST
url_add = os.getenv("api_url")
user = {
    "name": "Jorge Bianculli"
}
r = requests.post(url_add, timeout=10, data=user)
print("POST", r)


# hacer un PUT
url_del = os.getenv("api_url")
url_del = url_del + "/2"
user = {
    "name": "Antonio"
}
r = requests.put(url_del, timeout=10, data=user)
print("PUT", r)


# hacer un DELETE
url_del = os.getenv("api_url")
url_del = url_del + "/3"
r = requests.put(url_del, timeout=10)
print("DELETE", r)


# apis protegidas
url_del = os.getenv("api_url")
url_del = url_del + "/3"
apikey = "123456789"
headers = {
    "Authorization": f"Bearer {apikey}"
}
r = requests.put(url_del, timeout=10, headers=headers)
print("DELETE", r)
