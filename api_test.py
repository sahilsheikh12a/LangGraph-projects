from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()
# Create model
llm = ChatOpenAI(model="gpt-4o-mini")

# Send test message
response = llm.invoke("hii how are you")

print(response.content)