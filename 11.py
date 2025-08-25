
from langchain_gigachat.chat_models import GigaChat
from fastapi import FastAPI

app = FastAPI()
@app.get("/")
def home():
    return {"message": "Text Recognition API"}

# Создаём модель
model = GigaChat(
    model="GigaChat-2-Max",
    verify_ssl_certs=False,
    credentials="=="
)

# Загружаем изображение
image_path = input("Введите путь к изображению: ")
with open(image_path, "rb") as image_file:
    file_uploaded_id = model.upload_file(image_file).id_

# Отправляем файл на распознование
message = {
    "role": "user",
    "content": "Распознай текст с этого изображения. Найди в нем название компании(name), телефоны(phones), email, адреса и сохрани их в формате JSON: {\"name\": \"\", \"phones\": [], \"email\": \"\", \"address\": \"\", \"description\": \"\"}. Верни только JSON без дополнительного текста.",
    "attachments": [file_uploaded_id]
}

response = model.invoke([message])
# Выводим результат
print("\nРаспознанный текст:")
print("-" * 50)
print(response.content)
print("-" * 50)


