from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Industrial Loan API is running"}