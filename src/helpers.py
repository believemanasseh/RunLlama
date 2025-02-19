"""Basic utility functions."""

from collections.abc import Iterator

from ollama import ChatResponse, chat


def get_chat_response(model: str, prompt: str) -> Iterator[ChatResponse]:
	"""Returns chat response."""
	return chat(
		model=model,
		messages=[
			{
				"role": "user",
				"content": prompt,
			},
		],
		stream=True,
	)
