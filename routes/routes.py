from itertools import product
#from azure_blob_functions.blob import get_blob, upload_blob#, delete_blob, download_blob, get_blob
from fastapi import APIRouter, Form, UploadFile, File
#from azure_blob_functions.blob import upload_blob,get
from schema.product_schema import Product_Schema, Client_Schema, Sucursal_Shcema, Inventory_Schema
from config.db import conn
from models.product import product,client, sucursales, inventory
from repositories.postgres_repository import repository_postgres
from services.azure_services import get_blob, upload_blob

blob_routes = APIRouter()
#Product = APIRouter()

######## crear tablas
@blob_routes.post("/product")
#repository_postgres.create_client()



@blob_routes.post("/inventory")



@blob_routes.post("/sucursal")



@blob_routes.post("/client")


############# subir archivos a azure
@blob_routes.post("/upload")
async def upload(container: str = Form(...), file: UploadFile = File(...)):
    data = await file.read()
    filename = file.filename
    return upload_blob(filename, container, data)

@blob_routes.get("/file/{container}/{filename}")
def get_file(container: str, filename: str):
    return get_blob(filename, container)

