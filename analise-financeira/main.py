"""Fornecer acesso a cotações de ações,
    índices de mercado, taxas de câmbio, 
    commodities e outros dados financeiros em tempo real e histórico. 
    
    Esses dados são cruciais para análise de investimentos, 
    monitoramento de portfólios e tomada de decisões informadas."""
    

from pydantic import BaseModel
from fastapi import FastAPI, HTTPException
import requests

app = FastAPI()


# class User(BaseModel):
#     id: int
#     name: str


API_TOKEN = 'jrfFdSF8RZ1scxbTk8baH7'
API_URL = f'https://brapi.dev/api/quote/PETR4?'

# https://brapi.dev/api/quote/{ticker}?token={seu_token}
# Substitua {ticker} pelo símbolo da ação que você está interessado.

### Atualizaar a api pra q seja passado a acao e seja retornado as infos dessa acao em expecifico


@app.get('/financeiro')
async def get_dados():
    headers = {'Authorization': f"Bearer {API_TOKEN}"}
    try:
        response = requests.get(API_URL, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            raise HTTPException(status_code=response.status_code, detail=response.text)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
