from langchain_ollama import ChatOllama
# from langchain_core.output_parsers import StrOutputParser
from langchain.chat_models import init_chat_model

def diff_model_responses(question: str, model_names: list[str]) -> dict[str, str]:
    responses = {}
    for model_name in model_names:
        model = init_chat_model(
            model = model_name,
            temperature = 0.7,
            streaming = False,
            model_provider = 'ollama',
            base_url = 'http://localhost:11434'
        )
        response = model.invoke(question)
        responses[model_name] = response
    return responses 

results = diff_model_responses("What is AI?", ['llama3.2:latest','qwen3:0.6b','qwen2.5:14b'])
for model, answer in results.items():
    print(f"Reponse from{model}: {answer.content}\n")

if __name__ == "__main__":
    diff_model_responses()