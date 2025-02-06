# RunLlama

Simple CLI tool for [Ollama (LLM) models](https://ollama.com/search).

## Installation

Install via pip:

```bash
pip install runllama
```

Or with Poetry:

```bash
poetry add runllama
```

Run the CLI:

```bash
runllama --help
```

## For Development

Build and run ollama server docker container

```bash
docker build -t runllama .
docker run -d -p 11434:11434 -v ollama:/app/.ollama --name runllama runllama 
```

Install dependencies

```bash
poetry install
poetry shell
```

Run Python script

```bash
python src/main.py --help
```

## License

The extension source code is licensed under the MIT License (see [LICENSE](LICENSE)).
