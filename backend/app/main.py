from fastapi import FastAPI

app = FastAPI(title="Inventarios API")

@app.get("/")
def root():
    return {"status": "ok"}
