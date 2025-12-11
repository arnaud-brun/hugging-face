# Readme


## Setup

Requirements:
 - Python >= 3.10

Install dependencies:
```bash
PIPENV_VENV_IN_PROJECT=1 pipenv --python 3.10 install huggingface_hub smolagents ddgs opentelemetry-sdk opentelemetry-exporter-otlp openinference-instrumentation-smolagents langfuse
```

Setup the .env file:
```bash
HF_TOKEN=...
LANGFUSE_SECRET_KEY=...
LANGFUSE_PUBLIC_KEY=...
LANGFUSE_BASE_URL=...
```

## Scripts

```bash
# Run the app
pipenv run app

# Load Agent from hub
pipenv run load
```

