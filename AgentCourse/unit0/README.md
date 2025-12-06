# Onbaording

## To read later

 - [Free NLP course](https://huggingface.co/learn/llm-course/chapter1/1)
 - [chat_templating](https://huggingface.co/docs/transformers/main/en/chat_templating)
 - [Transformers](https://huggingface.co/docs/transformers/index)


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

