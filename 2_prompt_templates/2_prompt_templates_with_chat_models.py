from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

# PART 1: Create a ChatPromptTemplate using a template string
print("-----Prompt from Template-----")
template = "Tell me a joke about {topic}."
prompt_template = ChatPromptTemplate.from_template(template)
prompt = prompt_template.invoke({'topic':'dog'})
result = model.invoke(prompt)
print(result.content)

# PART 2: Prompt with Multiple Placeholders
print("\n----- Prompt with Multiple Placeholders -----\n")
template_multiple = """You are a helpful assistant.
Human: Tell me a {adjective} short story about a {animal}.
Assistant:"""
prompt_multiple = ChatPromptTemplate.from_template(template_multiple)
prompt = prompt_multiple.invoke({"adjective": "funny", "animal": "panda"})

result = model.invoke(prompt)
print(result.content)

# PART 3: Prompt with System and Human Messages (Using Tuples)
print("\n----- Prompt with System and Human Messages (Tuple) -----\n")
messages = [
    ("system", "You are a comedian who tells jokes about {topic}."),
    ("human", "Tell me {joke_count} jokes."),
]
prompt_template = ChatPromptTemplate.from_messages(messages)
prompt = prompt_template.invoke({"topic": "lawyers", "joke_count": 3})
result = model.invoke(prompt)
print(result.content)

"""
Here note that, we need to call invoke function twice 
First we need to create prompt template and from prompt_template we need to create prompt
by passing input variables using 'invoke' function and then we need to pass that prompt 
when we are invoking model using model.invoke
but with 'Chains' these gets easier. 

"""