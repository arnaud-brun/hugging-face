# Onbaording

## To read later


## HuggingFace
 - [Free NLP course](https://huggingface.co/learn/llm-course/chapter1/1)
 - [Transformers](https://huggingface.co/docs/transformers/index)
 - [chat_templating](https://huggingface.co/docs/transformers/main/en/chat_templating)
 - [Models timeline](https://huggingface.co/docs/transformers/models_timeline)
 - [SmolAgents](https://huggingface.co/docs/smolagents)
 - [Secure Code Execution](https://huggingface.co/docs/smolagents/tutorials/secure_code_execution)
 - [Agent guidelines](https://huggingface.co/docs/smolagents/tutorials/building_good_agents)
 - [Building effective agent](https://www.anthropic.com/research/building-effective-agents)
 - [MCP](https://huggingface.co/learn/mcp-course/unit1/architectural-components)
 

### Ecosystem
 - [LangGraph](https://langchain-ai.github.io/langgraph/)
 - [Retrieval Augmented Generation (RAG)](https://www.pinecone.io/learn/retrieval-augmented-generation/)

### Misc
 - [Pipfile - What is the perfect 'requirements.txt' file ?]







## Setup


### Ollama

Starting Ollama from Docker (MacOS is too old):
```bash
docker run -d -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama
```

Pulling qwen2:7b locally:
```bash
docker exec -it ollama ollama run qwen2:7b
```

### Smolagents

Requirements:
 - Python >= 3.10

Setting up python project locally:
```bash
PIPENV_VENV_IN_PROJECT=1 pipenv --python 3.10 install "smolagents[litellm]"

pipenv run python main.py
```

