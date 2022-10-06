from schema.product_schema import Product_Schema, Client_Schema, Sucursal_Shcema, Inventory_Schema
from models.product import product,client, sucursales, inventory
from config.db import conn


class repository_postgres:
    def create_product(data_product: Product_Schema):
        new_product = data_product.dict()
        conn.execute(product.insert().values(new_product))
        return "success"

    def create_inventory(data_inventory: Inventory_Schema):
        new_inventory = data_inventory.dict()
        conn.execute(inventory.insert().values(new_inventory))
        return "success"

    def create_sucursal(data_sucursal: Sucursal_Shcema):
        new_sucursal = data_sucursal.dict()
        conn.execute(sucursales.insert().values(new_sucursal))
        return "success"

    def create_client(data_client: Client_Schema):
        new_client = data_client.dict()
        conn.execute(client.insert().values(new_client))
        return "success"

    def schema_product(gtin_product, preciounidad):
        pass



