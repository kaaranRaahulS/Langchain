#Disabled inline suggestion
from langchain-ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


def main():
    model = ChatOllama(
        model="qwen2.5:14b",      
        base_url="http://localhost:11434", 
        temperature=0.7,
    )
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful assistant. Answer in one word. Always respond in English."),
        ("human", "{input}"),
    ])

    parser = StrOutputParser()

    #chaining prompt, model and parser using | (pipe)
    chain = prompt | model | parser

    result = chain.invoke({"input": "What is the capital of paris?"}) 

    print(result)

if __name__ == "__main__":
    main()