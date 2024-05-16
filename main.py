from fastapi import FastAPI
from database import engine
import models as models
from routers import blog, user, ejemplo

app = FastAPI()
models.Base.metadata.create_all(bind=engine)

@app.get("/", tags=["Raiz"])
def index():
    return {"message": "Hello, World!"}

# Seccion API
app.include_router(blog.router)
app.include_router(user.router)
app.include_router(ejemplo.router)
