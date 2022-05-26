from fastapi import FastAPI
from pydantic import BaseModel
from collections import defaultdict
from cd_spacy import spacy_load_sm

nlp = spacy_load_sm()
app = FastAPI()
# A simple class that represents a search response.
class search_resp:
    def __init__(self, input, result):
        self.input = input
        self.result = result

# A base model that represents a search request.
class search_req(BaseModel):
    input = ''


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/ner/")
async def name_entity_recognition(req: search_req):
    doc = nlp(req.input)
    result = defaultdict(list)
    for entity in doc.ents:
        result[entity.label_].append(entity.text)
    return search_resp(input = req.input, result = result)