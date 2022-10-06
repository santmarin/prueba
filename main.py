
from fastapi import FastAPI
from routes.routes import blob_routes
#from routes.routes import Product


app = FastAPI()
app.include_router(blob_routes)


