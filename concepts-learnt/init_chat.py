from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.chat_models import init_chat_model

from langchain.messages import HumanMessage, SystemMessage, AIMessage
from langchain_ollama import ChatOllama

def demo_init_chat_model():
    chat_model = init_chat_model(
        model = "qwen2.5:14b",
        temperature = 0.7,
        streaming = True, 
        max_retries = 3,
        base_url="http://localhost:11434",
        model_provider = "ollama"
    )
    response = chat_model.invoke("What's the capital of france. Answer in one word.")
    print(f"Response {response.content}")

if __name__ == "__main__":
    demo_init_chat_model()