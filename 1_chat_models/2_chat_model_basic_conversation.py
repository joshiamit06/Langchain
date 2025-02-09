"""
Mainly 3 types of messages 

 SystemMessage:
   Message for priming AI behavior, usually passed in as the first of a sequenc of input messages.
 HumanMessagse:
   Message from a human to the AI model.
 AIMessage:
   Message from an AI.
"""

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

# System message always comes the first.
messages = [
    SystemMessage(content="Solve the following math problem"),
    HumanMessage(content="what is 81 devided by 9?")
]

#invoke the model with messages
result = model.invoke(messages)
print("Answer from AI: ", result.content)


# AIMessage:
#   Message from an AI.
messages = [
    SystemMessage(content="Solve the following math problems"),
    HumanMessage(content="What is 81 divided by 9?"),
    AIMessage(content="81 divided by 9 is 9."),
    HumanMessage(content="What is 10 times 5?"),
]

# Invoke the model with messages
result = model.invoke(messages)
print(f"Answer from AI: {result.content}")