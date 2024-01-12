from typing import Union
from fastapi import FastAPI
from nslookup import Nslookup

app = FastAPI()

@app.get("/")
def root():
    return("Hello World")

@app.get("/domain/{domain}")
def check_domain(domain: str):
    dns_query = Nslookup()
    dns_info = dns_query.dns_lookup(domain)

    return (dns_info.answer)