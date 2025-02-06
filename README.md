# RunLlama

Simple CLI tool for [Ollama models](https://ollama.com/search).

## Usage

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
  cd runner
  python main.py --help
```
