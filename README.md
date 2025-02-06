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

1.) Build and run ollama server docker container

```bash
docker build -t runllama .
docker run -p 11434:11434 -d --name runllama runllama 
```

2.) Install dependencies

```bash
poetry install
poetry shell
```

3.) Run Python script

```bash
python src/main.py --help
```

## License

The extension source code is licensed under the MIT License (see [LICENSE](LICENSE)).
