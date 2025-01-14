from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import Path
from string import Template
import smtplib

plantilla = Path("paquetes-nativos/plantilla.html").read_text("utf-8")
template = Template(plantilla)
cuerpo = template.substitute({"usuario": "Jorge"})


path = Path("paquetes-nativos/python.png")
mime_image = MIMEImage(path.read_bytes())

mensaje = MIMEMultipart()
mensaje["from"] = "jbianculli.py"
mensaje["to"] = "jabianculli@gmail.com"
mensaje["subject"] = "email desde Python"
cuerpo = MIMEText(cuerpo, "html")
mensaje.attach(cuerpo)
mensaje.attach(mime_image)

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("jabianculli", "eegidziqdshhuxzh")
    smtp.send_message(mensaje)
