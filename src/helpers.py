"""Basic utility functions."""

from ollama import ChatResponse, chat


def get_chat_response(model: str, prompt: str) -> ChatResponse:
	"""Returns chat response."""
	return chat(
		model=model,
		messages=[
			{
				"role": "user",
				"content": prompt,
			},
		],
	)
