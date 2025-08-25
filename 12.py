
from langchain_gigachat.chat_models import GigaChat
from fastapi import FastAPI, File, UploadFile
import json

app = FastAPI()

model = GigaChat(
    model="GigaChat-2-Max",
    verify_ssl_certs=False,
    credentials="MjY5NzhmNDItYjU4Ny00Y2ZlLTgzOTUtMjIyYzA3NzQzZGYwOjZkOTYyOThkLTE5YzEtNGVhNC05ZmEyLTA1ZTkxZGE5OTE1Mg=="
)

@app.get("/")
def home():
    return {"message": "Text Recognition API"}

@app.post("/analyze")
async def analyze_image(file: UploadFile = File(...)):
    file_uploaded_id = model.upload_file(file.file).id_
    
    message = {
        "role": "user",
        "content": "Распознай текст с этого изображения. Найди в нем название компании(name), телефоны(phones), email, адреса и сохрани их в формате JSON: {\"name\": \"\", \"phones\": [], \"email\": \"\", \"address\": \"\", \"description\": \"\"}. Верни только JSON без дополнительного текста.",
        "attachments": [file_uploaded_id]
    }
    
    response = model.invoke([message])
    
    try:
        result = json.loads(response.content)
        return result
    except:
        return {"error": "Не удалось распарсить JSON", "raw_response": response.content}


