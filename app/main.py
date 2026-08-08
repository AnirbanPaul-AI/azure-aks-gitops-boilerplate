from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Hello from Azure AKS! Version 1 - Status 2"}
@app.get("/health")
def health():
    return {"status": "ok"}
