
from langchain_gigachat.chat_models import GigaChat

'''
pip install langchain>=0.3.25
pip install langchain-gigachat>=0.3.10
'''

model = GigaChat(
    model="GigaChat-2-Max",
    verify_ssl_certs=False,
    credentials="=="
)

#message = model.invoke("Привет, как дела?")

#message = {"role": "user", "content": "Привет, как дела?"}
#response = model.invoke([message])
#print(response.content)

#message = {"role": "assistant", "content": response.content}

#message = {"role": "user", "content": "Прогноз погоды в Москве на 10 дней."}
#response = model.invoke([message])
#print(response.content)

message = {
    "role": "user",
    "content": "Распознай текст с этого изображения и выведи его полностью.",
    "attachments": ["Image20250825114326.png"]
}

with open("Image20250825114326.png", "rb") as image_file:
    file_uploaded_id = model.upload_file(image_file).id_
    
response = model.invoke([message])
print(response.content)
# не работает