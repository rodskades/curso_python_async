from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Produto(BaseModel):
    id: int
    nome: str
    preco: float
    em_oferta: float = False


produtos = [
    Produto(id=1, nome='Playstation 5', preco=5745.55, em_oferta=True),
    Produto(id=2, nome='Nintendo Wii', preco=2678.00),
    Produto(id=3, nome='Xbox 360', preco=1999.55, em_oferta=True),
    Produto(id=4, nome='Super Nintendo', preco=345.35),
]


@app.get('/')
async def index():
    return {"Geek": "University"}


@app.get('/produtos/{id}')
async def buscar_produto(id: int):
    for produto in produtos:
        if produto.id == id:
            return produto
    return None


@app.put('/produtos/{id}')
async def atualizar_produto(id: int, produto: Produto):
    for prod in produtos:
        if prod.id == id:
            prod = produto

            return prod
    return None

