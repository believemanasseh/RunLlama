"""Setup for packaging and distribution."""

from setuptools import setup

with open("README.md", encoding="utf-8") as fh:
	long_description = fh.read()

setup(
	name="runllama",
	version="0.2.0",
	author="Believe Manasseh",
	author_email="believemanasseh@gmail.com",
	description="Simple CLI runner for Ollama (LLM) models",
	long_description=long_description,
	long_description_content_type="text/markdown",
	packages=["src"],
	install_requires=["ollama>=0.4.7", "click>=8.0.0"],
	classifiers=[
		"Programming Language :: Python :: 3.10",
		"Programming Language :: Python :: 3.11",
		"Programming Language :: Python :: 3.12",
		"Programming Language :: Python :: 3.13",
		"Programming Language :: Python :: 3.14",
		"Operating System :: OS Independent",
		"Development Status :: 5 - Production/Stable",
	],
	python_requires=">=3.10",
)
