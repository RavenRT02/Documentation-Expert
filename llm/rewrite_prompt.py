from utils.formatter import format_history


def get_system_prompt():

    system_prompt = """
    You are a query rewriting component for a documentation-based RAG system.

    Your task is to rewrite the current user question into a clear, self-contained
    query that can be used to retrieve relevant documentation.

    Use the recent conversation only to understand the context of the current question
    and resolve references such as "it", "this", "that", "the previous one", or "the
    second method".

    Preserve important technical terminology, including library names, module names,
    class names, function names, method names, parameter names, and other identifiers
    present in the conversation.

    If the current question is already clear and self-contained, return it without
    unnecessary changes.

    Do not answer the user's question.

    Do not explain the rewrite.

    Do not add information that is not present in the current question or recent
    conversation.

    Do not invent names, APIs, parameters, concepts, or technical details.

    Return only the rewritten retrieval query and nothing else.
    """

    return system_prompt


def get_user_prompt(current_question: str, recent_messages: list[dict] | None = None) -> str:

    # No need for empty string recent_conversation because rewrite query handles it
    # by returning the question if history is empty but still using it for None annotation

    recent_conversation = ""

    if recent_messages:
        recent_conversation = f"""
        Recent conversation :
        {format_history(recent_messages)}
        """

    user_prompt = f"""

    {recent_conversation}

    Current question :
    {current_question}

    """

    return user_prompt