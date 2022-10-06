from ast import Try
from codecs import utf_8_decode
from typing import BinaryIO, ByteString
from azure.storage.blob import BlobServiceClient
from os import getenv
from binascii import hexlify
from array import array
from pydantic import ConfigError
from responses.response_json import response_json
import csv
from symbol import try_stmt
from azure_blob_functions.blob import blob_service_client
import sys
import ast
# data1 = []
# data2 = []


def upload_blob(filename: str, container: str, data: BinaryIO):
    try:
        blob_client = blob_service_client.get_blob_client(container=container, blob=filename)

        blob_client.upload_blob(data)

        return response_json(message="succes")
    except Exception as e:
        return response_json(message=e.message, status=500)

def get_blob(filename: str, container: str):
    try:
        blob_client = blob_service_client.get_blob_client(container=container, blob=filename)
    
        blob_data = blob_client.download_blob().readall()
        data_blob = blob_data.decode('UTF-8')
        data = data_blob.split(',')
        datos = {}
        j = 0
        while j<19:
            for i in data:
                dt = data[i]
            datos = dt
        print(datos)    



    except Exception as e:
        print(e)
        return "response_json(message=e.message, status=500)"