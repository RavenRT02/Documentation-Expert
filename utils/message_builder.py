def build_messages(system_prompt: str, user_prompt: str | None = None) -> list[dict]:
    """
    Take the system and user prompts to build
    messages format for llms
    """

    messages = [
        {
            "role" : "system",
            "content" : system_prompt
        }
    ]

    if user_prompt is not None:
        messages.append(
            {
                "role" : "user",
                "content" : user_prompt
            }
        )

    return messages