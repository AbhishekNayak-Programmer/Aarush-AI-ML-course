import os 

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

if not os.getenv("OPENAI_API_KEY"):
    raise ValueError("OPENAI_API_KEY is missing from .env")


model = ChatOpenAI(model="gpt-4.1-mini", temperature=0)

response = model.invoke("Explain Python Lists in simple words with example")

print(response.content)