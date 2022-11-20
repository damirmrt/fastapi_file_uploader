from fastapi import FastAPI, Body, Cookie
from fastapi.responses import Response


app = FastAPI()


@app.get("/")
def index_page():
    return Response('hello world', media_type="text/html")


@app.post("/upload")
def login_process():
    return Response('hello world', media_type="text/html")