import click
from ollama import ChatResponse, ResponseError
from ollama import pull as pull_model

from .helpers import get_chat_response


@click.group()
def runner():
    """Large language model runner"""
    pass


@runner.command()
@click.option(
    "--model", "-m", type=str, default="deepseek-r1:1.5b", help="Name of model"
)
@click.argument("prompt", type=str)
def query(model: str, prompt: str) -> None:
    """Query LLM"""

    try:
        response: ChatResponse = get_chat_response(model, prompt)
    except ResponseError as e:
        click.echo(e)
        if e.status_code == 404:
            pull_model(model)  # Pulls model from registry
            response: ChatResponse = get_chat_response(model, prompt)
    except Exception as e:
        click.echo(e)
        exit()

    click.echo(response["message"]["content"])


@runner.command()
@click.argument("model", type=str)
def pull(model: str):
    """Pull a model from registry"""
    try:
        click.echo(f"Pulling model: {model}")
        pull_model(model)
    except Exception as e:
        click.echo(e)
        exit()


if __name__ == "__main__":
    runner()
