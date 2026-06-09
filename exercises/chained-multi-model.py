from langchain_ollama import ChatOllama

from langchain_core.output_parsers import StrOutputParser
from langchain.chat_models import init_chat_model

def multi_model_response(question: str, model_name: list[str]) -> dict[str,str]:
    responses = {}
    for model in model_name:
        chat_model = init_chat_model(
            model = model,
            temperature = 0.7,
            model_provider = "ollama",
            base_url = "http://localhost:11434"
        )
        response = chat_model.invoke(question)
        responses[model] = answer.content
    return responses



if __name__ == "__main__":
    main()