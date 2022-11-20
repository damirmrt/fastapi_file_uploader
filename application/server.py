from fastapi import FastAPI, File, UploadFile
from fastapi.responses import Response


app = FastAPI()


@app.get("/")
def index_page():
    with open(file=".\\templates\index.html", encoding="utf-8") as html_file:
        html_page = html_file.read()
    return Response(html_page, media_type="text/html")


@app.post("/upload/")
def upload(file: UploadFile = File(...)):
    file_content = file.file.read()
    with open(file.filename, 'wb') as f:
        # PUT YOUR MAGIC HERE
        f.write(file_content)
    file.file.close()
    return Response(f"Successfully uploaded and processed {file.filename}", media_type="text/html")