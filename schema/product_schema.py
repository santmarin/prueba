from pydantic import BaseModel

class Product_Schema(BaseModel):
    Gtin_product: str
    PrecioUnidad: str

class Inventory_Schema(BaseModel):
    FechaInventario: str
    Gtin_product: str
    gln_sucursal: str
    InventarioFinal: str

class Sucursal_Shcema(BaseModel):
    gln_sucursal: str


class Client_Schema(BaseModel):
    gln_client: str