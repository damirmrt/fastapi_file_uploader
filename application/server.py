from fastapi import FastAPI, File, UploadFile
from fastapi.responses import Response


app = FastAPI()


@app.get("/")
def index_page():
    with open(file=".\\templates\index.html", encoding="utf-8") as html_file:
        html_page = html_file.read()
    return Response(html_page, media_type="text/html")


@app.post("/upload/")
def login_process():
    async def create_upload_file(file: UploadFile):
        return {"filename": file.filename}