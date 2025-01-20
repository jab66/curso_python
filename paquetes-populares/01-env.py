# variables de entorno

from dotenv import load_dotenv
import os

load_dotenv()
print(os.getenv("api_key"))
print(os.getenv("api_name"))
