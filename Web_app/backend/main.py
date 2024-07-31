# backend/main.py
from fastapi import FastAPI, HTTPException,  Response, Depends
import orjson
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import pandas as pd
import os
import json
from typing import Any, Dict, List
from fastapi_pagination import Page, paginate, add_pagination
from pydantic import BaseModel
from pprint import pprint



origins = [
    "http://localhost:8080",
    "http://192.168.169.150:8080",
]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.get("/")
async def read_root():
    return {"message": "Hello, World!"}

@app.get("/search-ip")
async def sear():
    return {"message": 'search-ip'}


def getfilename(rec_id):
    file_path = "../frontend/src/assets/files/"
    filename = [filename for filename in os.listdir(file_path) if rec_id.lower() in filename.lower()]
    file_address = file_path+filename[0]
    return file_address

# @app.get("/reconcile/{rec_id}")
# async  def get_reconcile(rec_id: str) -> Page[Dict]:
#     file_address = getfilename(rec_id)

#     if not os.path.exists(file_address):
#         raise HTTPException(status_code=404, detail="File not found")

#     df = pd.read_excel(file_address)
#     data = df.to_dict(orient="records")
#     paginated_items = paginate(data)

#     return paginated_items


@app.get("/reconcile/{rec_id}")
async  def get_reconcile(rec_id: str):
    file_address = getfilename(rec_id)

    if not os.path.exists(file_address):
        raise HTTPException(status_code=404, detail="File not found")
    
    sheets = pd.ExcelFile(file_address).sheet_names
    return sheets

@app.get("/reconcile/{rec_id}/{sheet_name}", response_model=Page[dict])
def get_sheet_data(rec_id: str, sheet_name: str, page: int = 1, page_size: int = 10):
    file_address = getfilename(rec_id)
    df = pd.read_excel(file_address, sheet_name=sheet_name)
    data = df.to_dict(orient='records')
    return paginate(data)

add_pagination(app)

