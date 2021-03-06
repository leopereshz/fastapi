from typing import Optional

from fastapi import Depends, FastAPI

app = FastAPI()


#permite criar um modelo de parâmetros comuns para ser reaproveitado
#em várias funções, como consultas.

async def common_parameters(q: Optional[str] = None, skip: int = 0, limit: int = 100):
    return {"q": q, "skip": skip, "limit": limit}


@app.get("/items/")
async def read_items(commons: dict = Depends(common_parameters)):
    return commons


@app.get("/users/")
async def read_users(commons: dict = Depends(common_parameters)):
    return commons