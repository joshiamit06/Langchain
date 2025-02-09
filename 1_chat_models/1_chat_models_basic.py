from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI

load_dotenv()
# model = ChatOpenAI(model="gpt-4o")
model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

result = model.invoke("what is 81 devided by 9?")
print("full result:")
print(result)
print("content only:")
print(result.content)

