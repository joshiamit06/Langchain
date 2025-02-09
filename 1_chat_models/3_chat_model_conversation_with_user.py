from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

load_dotenv()

# Create a gemini model
model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

chat_history = [] # use to store messages

# Set an initial system message
system_message = SystemMessage(content="You are an helpful AI assistant")
chat_history.append(system_message)

#Chat starts

while True:
    query = input("You: ")
    if "exit" in query.lower():
        break
    chat_history.append(HumanMessage(content=query)) # Add user message

    # GenAi responds using chat history
    result = model.invoke(chat_history)
    response = result.content
    chat_history.append(AIMessage(content=response))  # Add AI message 

    print("AI message:" , response)

print("----Chat History----")
print(chat_history)
