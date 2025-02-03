"""
    Fornecer acesso a cotações de ações,
    índices de mercado, taxas de câmbio, 
    commodities e outros dados financeiros em tempo real e histórico.
"""

from pydantic import BaseModel
from fastapi import FastAPI, HTTPException
import requests

app = FastAPI()


API_TOKEN = 'jrfFdSF8RZ1scxbTk8baH7'
API_URL = f'https://brapi.dev/api/quote/'


@app.get('/acao')
async def get_acoes(acao: str):
    headers = {'Authorization': f"Bearer {API_TOKEN}"}
    try:
        
        response = requests.get(API_URL+acao, headers=headers)
        
        nome_acao = response.json().get('results')[0].get('longName')
        result = response.json().get('results')[0]
        if response.status_code == 200:
            return {"status": "success", f"ação {nome_acao}": result}
        else:
            raise HTTPException(status_code=response.status_code, detail=response.text)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
