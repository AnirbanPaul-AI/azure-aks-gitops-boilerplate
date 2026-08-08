from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "GitOps AKS Boilerplate Running!"}

@app.get("/health")
def health():
    return {"status": "healthy"}
