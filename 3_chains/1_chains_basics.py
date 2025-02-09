"""
Chains are nothing more than tieing together a series of tasks.
Earlier we are using invoke function to create prompts also 
we are using it to chat model to respond to us.
Instead of this what we can do is prompt output we chain to as a input to the model and 
output of model is chained to input to someother item like this.
See theory doc to have flow diagram


LangChain Expression Language (LCEL)

chain = prompt | model

result = chain.invoke({"key":"value"})
"""

from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI

# Load environment variables from .env
load_dotenv()

# Create a model
model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

# Define prompt templates (no need for separate Runnable chains)
prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a comedian who tells jokes about {topic}."),
        ("human", "Tell me {joke_count} jokes."),
    ]
)

# Create the combined chain using LangChain Expression Language (LCEL)
chain = prompt_template | model | StrOutputParser()
# chain = prompt_template | model

####StrOutputParser is used to parse the output from the result. 
####we usually do result.content to get exact model response
####It is nearly same of doing result.content

# Run the chain
result = chain.invoke({"topic": "lawyers", "joke_count": 1})

# Output
print(result)


###########
## If we dont use chain then this is how we have to do this for the same ex.
# PART 3: Prompt with System and Human Messages (Using Tuples)
# print("\n----- Prompt with System and Human Messages (Tuple) -----\n")
# messages = [
#     ("system", "You are a comedian who tells jokes about {topic}."),
#     ("human", "Tell me {joke_count} jokes."),
# ]
# prompt_template = ChatPromptTemplate.from_messages(messages)
# prompt = prompt_template.invoke({"topic": "lawyers", "joke_count": 3}) ## Invoking to create prompt
# result = model.invoke(prompt)                                          ## invoking to get model response
# print(result.content)