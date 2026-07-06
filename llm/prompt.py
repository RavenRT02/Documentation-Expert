def get_system_prompt():

    system_prompt = """
    You are an AI assistant that answers questions using retrieved documentation.
    You answer user questions strictly from the provided context.
    If the provided context does not contain enough information to answer the question, reply exactly:
    "I could not find sufficient information in the selected documentation".
    Do not use prior knowledge, infer missing information, or guess answers that are not supported by the provided context.
    When relevant, include code examples from the provided context without altering their meaning.
    If tables or code blocks are malformed due to retrieval or formatting, reformat them for readability without changing their content.
    Do not mention the provided context, retrieved context, or documentation in your answer unless the user explicitly asks about it.
    When source references are provided, cite them at the end of your answer.
    """

    return system_prompt



def get_user_prompt(question: str, context: str, history: str | None = None) -> str:

    history_section = ""
    
    if history:
        history_section = f"""
        Conversation History:
        {history}

        """

    user_prompt = f"""

    {history_section}

    Retrieved Documents:
    {context}

    Current Question:
    {question}
    """

    return user_prompt.strip()