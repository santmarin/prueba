from ast import Try
from codecs import utf_8_decode
from typing import BinaryIO, ByteString
from azure.storage.blob import BlobServiceClient
from os import getenv
from responses.response_json import response_json
import csv
from symbol import try_stmt

from responses.response_stream import response_stream

blob_service_client = BlobServiceClient.from_connection_string(getenv("AZURE_STORAGE_CONNECTION_STRING"))

# def upload_blob(filename: str, container: str, data: BinaryIO):
#     try:
#         blob_client = blob_service_client.get_blob_client(container=container, blob=filename)

#         blob_client.upload_blob(data)

#         return response_json(message="succes")
#     except Exception as e:
#         return response_json(message=e.message, status=500)

# def get_blob(filename: str, container: str):
#     try:
#         blob_client = blob_service_client.get_blob_client(container=container, blob=filename)
    
#         blob_data = blob_client.download_blob().readall()
#         #print(blob_data)
#         data_blob =blob_data.decode('UTF-8')
#         # contenido = blob_data.split("\r\n")
#         # print(contenido)
#         #contennid = ByteString(blob_data)
#         print(data_blob)
#         # with open("./{filename}", "wb") as my_blob:
#         #     blob_data = blob_client.download_blob()
#         #     c = blob_data.readinto(my_blob)
#         #     print(c)
#             ##_#
#             #reader = csv.reader(my_blob)
#             #for row in reader:
#              #   print("fecha {0}, cliente {1}, sucursal {2}, producto {3}, invet {4}, precio {5}")
#         #return response_stream(data=blob_client.download_blob(), download=False)
#         #return response_json(message="succes")
#     except Exception as e:
#         print(e)
#         return "response_json(message=e.message, status=500)"

