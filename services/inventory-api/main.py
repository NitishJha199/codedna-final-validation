from fastapi import FastAPI

app = FastAPI()


@app.get("/health")
def health():
    return {"service": "inventory-api", "status": "ok"}
