from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

def main():
    model = ChatOllama(
        model = "qwen2.5:14b",
        temperature = 0.7,
        base_url="http://localhost:11434", 
    )

    prompt = ChatPromptTemplate.from_messages([
    "Create a marketing tagline for a product named '{product}' targeting '{audience}'."])
    parser  = StrOutputParser()

    chain = prompt | model | parser

    result = chain.invoke({"product":"AI Course", "audience":"developers"})

    print(f"Tagline: {result}")



if __name__ == "__main__":
    main()œ