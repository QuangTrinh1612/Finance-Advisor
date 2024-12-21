from langchain_openai import ChatOpenAI
from langchain.schema.messages import HumanMessage

llm: ChatOpenAI = ChatOpenAI(
    base_url="http://localhost:1234/v1",
    api_key="not-needed"
)

prompt = "What is Apple company?"
response = llm.invoke([HumanMessage(content=prompt)])
print(response.content)