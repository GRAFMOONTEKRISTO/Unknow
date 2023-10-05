import json
from builtins import str, int
from typing import Union

from fastapi import FastAPI

from api import ExtractorClient

app = FastAPI()
extractor = ExtractorClient()


@app.get("/passport")
async def get_extract_passport():
    passport_data = extractor.get_extract_passport()
    return json.loads(passport_data)


@app.get("/tax_accounting")
async def get_extract_tax_accounting():
    passport_data = extractor.get_extract_tax_accounting()
    return json.loads(passport_data)


@app.get("/snils")
async def get_extract_snils():
    passport_data = extractor.get_extract_snils()
    return json.loads(passport_data)


@app.get("/diploma")
async def get_extract_diploma():
    passport_data = extractor.get_extract_diploma()
    return json.loads(passport_data)


@app.get("/certificate_of_no_criminal_record")
async def get_extract_certificate_of_no_criminal_record():
    passport_data = extractor.get_extract_certificate_of_no_criminal_record()
    return json.loads(passport_data)

# app.get_extract_passport('qwe.png')
# app.format_check('qwe.png')
