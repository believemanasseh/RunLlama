"""This module contains base logic for all RunLlama actions."""

import sys
import time
from http import HTTPStatus

import click
from ollama import ResponseError
from ollama import pull as pull_model

from . import PROJECT_VERSION
from .helpers import get_chat_response


@click.group()
@click.version_option(PROJECT_VERSION, "--version", "-v", message="RunLlama v%(version)s")
def runner() -> None:
	"""Large language model runner"""


@runner.command()
@click.option("--model", "-m", type=str, default="deepseek-r1:1.5b", help="Name of model")
@click.argument("prompt", type=str)
def query(model: str, prompt: str) -> None:
	"""Query LLM"""
	try:
		response = get_chat_response(model, prompt)
	except ResponseError as e:
		click.echo(e)
		if e.status_code == HTTPStatus.NOT_FOUND:
			click.echo(f"Pulling model [{model}]...")
			pull_model(model)  # Pulls model from registry
			time.sleep(5)
			try:
				response = get_chat_response(model, prompt)
			except ResponseError as e:
				click.echo(e)
				click.echo("Exiting...")
				sys.exit(1)
	except Exception as e:
		click.echo(e)
		sys.exit(1)

	click.echo(response["message"]["content"])


@runner.command()
@click.argument("model", type=str)
def pull(model: str) -> None:
	"""Pull a model from registry"""
	try:
		click.echo(f"Pulling model: {model}")
		pull_model(model)
		click.echo("Model pulled successfully!")
	except Exception as e:
		click.echo(e)
		sys.exit(1)


if __name__ == "__main__":
	runner()
