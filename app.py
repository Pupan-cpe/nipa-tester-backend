import os
import json
import base64
from nvision import ObjectDetection
import os
import json
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi import FastAPI, File, UploadFile,Request
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()




origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
model = ObjectDetection(api_key='cdb29f355cb4059995e05420dc8d963f657898bf3a5f2f5e7a88c58279f5e4a0a1c4c4cf874594b42e413fc45c425425ac')



x = ""
@app.post("/img")
async def get_body(request: Request):
    e = await request.json()
    # print(e)
    
    for key, value in e.items(): 
    #    print(value)
       x = value
       
    response = model.predict(x)
    print(response)
    data = json.dumps(response.json(), indent=4, sort_keys=True)
   
    return response.json()


