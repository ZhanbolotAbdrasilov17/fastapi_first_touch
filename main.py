import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/", summary="Главная ручка", tags=["Основные ручки"])
def main():
    return "Hello, World!"

if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)