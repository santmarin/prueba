from itertools import product
from msilib import Table
from sqlalchemy import Column, Table, column
from sqlalchemy.sql.sqltypes import Integer, String, DateTime
from config.db import engine, meta_data

product = Table("product",meta_data,
                Column("Gtin_product", String),
                Column("PrecioUnidad", Integer))

inventory = Table("Inventoy",meta_data,
                    Column("FechaInventario", DateTime),
                    Column("Gtin_product", String),
                    Column("gln_sucursal", String),
                    Column("InventarioFinal", Integer))

sucursales = Table("Sucursal",meta_data, Column ("gln_sucursal", String))

client = Table("Clients",meta_data, Column("gln_client", String))

meta_data.create_all(engine)
