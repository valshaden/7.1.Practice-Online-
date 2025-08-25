
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

