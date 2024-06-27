from fastapi import FastAPI

app = FastAPI()


@app.get("/home")
def read_root():
    return {"Hello": "World"}


@app.get("/about")
def about():
    return {"msg": "About Us"}


@app.get("/contact")
def contact():
    return {"email": "manepriyesh777@gmail.com", "phone": "8767565401"}

