# client.py - ejemplo minimal
import os
from zeep import Client
from zeep.helpers import serialize_object

WSDL = os.getenv("HKA_WSDL_URL") or "https://demointegracion.thefactoryhka.com.pa/ws/obj/v1.0/Service.svc?singleWsdl"
TOKEN_EMP = os.getenv("HKA_TOKEN_EMPRESA")
TOKEN_PWD = os.getenv("HKA_TOKEN_PASSWORD")

client = Client(wsdl=WSDL)

def enviar(documento: dict):
    resp = client.service.Enviar(TOKEN_EMP, TOKEN_PWD, documento)
    return serialize_object(resp)
