from importlib.metadata import metadata
from sqlalchemy import create_engine, MetaData

engine = create_engine("postgresql://postgres:postgres@localhost:5432/postgres")

conn = engine.connect()

meta_data = MetaData()
