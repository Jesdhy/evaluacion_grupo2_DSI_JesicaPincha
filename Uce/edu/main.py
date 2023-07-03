import uvicorn
from fastapi import FastAPI
from Uce.edu.OpenAI import Document, inference

app = FastAPI()


@app.get('/')
def read_root():
    return {'Hellow': 'World'}


@app.post('/inference', status_code=200)
def inference_endpoint(doc: Document):
    response = inference(doc.prompt)
    return {
        'inference': response[0],
        'usage': response[1]
    }


