"""Base test module."""

from click.testing import CliRunner
from src.main import pull, query

runner = CliRunner()
model = "deepseek-r1:1.5b"


def test_query():
	"""Test query feature."""
	result = runner.invoke(query, ["-m", model, "what is test?"])
	assert result.exit_code == 0


def test_pull():
	"""Test pull feature."""
	result = runner.invoke(pull, [model])
	assert result.exit_code == 0
