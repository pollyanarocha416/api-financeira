"""
    Fornecer acesso a cotações de ações,
    índices de mercado, taxas de câmbio, 
    commodities e outros dados financeiros em tempo real e histórico.
"""

from pydantic import BaseModel
from fastapi import FastAPI, HTTPException
import requests
from main_conf import API_URL, API_TOKEN



app = FastAPI()



@app.get('/acao')
async def get_acoes(acao: str):
    headers = {'Authorization': f"Bearer {API_TOKEN}"}
    try:
        
        response = requests.get(API_URL+acao, headers=headers)
        if response:
            nome_acao = response.json().get('results')[0].get('longName')
            result = response.json().get('results')[0]
            if response.status_code == 200:
                return {"status": "success", f"ação {nome_acao}": result}
            else:
                raise HTTPException(status_code=response.status_code, detail=response.text)
        else:
            raise HTTPException(status_code=404, detail="Ação não encontrada")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
