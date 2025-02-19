"""This module contains base logic for all RunLlama actions."""

import sys
import time
from http import HTTPStatus

import click
from ollama import ResponseError
from ollama import pull as pull_model

from src import PACKAGE_VERSION
from src.helpers import get_chat_response


@click.group()
@click.version_option(PACKAGE_VERSION, "--version", "-v", message="RunLlama v%(version)s")
def runner() -> None:
	"""Large language model runner"""


@runner.command()
@click.option("--model", "-m", type=str, default="deepseek-r1:1.5b", help="Name of model")
@click.argument("prompt", type=str)
def query(model: str, prompt: str) -> None:
	"""Query LLM"""
	try:
		stream = get_chat_response(model, prompt)
		for chunk in stream:
			click.echo(chunk.message.content, nl=False)
	except ResponseError as e:
		click.echo(e)
		if e.status_code == HTTPStatus.NOT_FOUND:
			try:
				# Pulls model from registry
				click.echo(f"pulling model: {model}")
				progress = pull_model(model, stream=True)
				for chunk in progress:
					click.echo(chunk.status)

				time.sleep(5)
				stream = get_chat_response(model, prompt)
				for chunk in stream:
					click.echo(chunk.message.content, nl=False)
			except ResponseError as e:
				click.echo(e)
				click.echo("exiting...")
				sys.exit(1)
			except Exception as e:
				click.echo(e)
				click.echo("exiting...")
				sys.exit(1)
	except Exception as e:
		click.echo(e)
		sys.exit(1)


@runner.command()
@click.argument("model", type=str)
def pull(model: str) -> None:
	"""Pull a model from registry"""
	try:
		click.echo(f"pulling model: {model}")
		progress = pull_model(model, stream=True)
		for chunk in progress:
			click.echo(chunk.status)
		click.echo("model pulled successfully!")
	except Exception as e:
		click.echo(e)
		sys.exit(1)


if __name__ == "__main__":
	runner()
