from llm.rewrite_prompt import get_system_prompt, get_user_prompt
from utils.message_builder import build_messages
from llm.model import generate_response


def rewrite_query(tokenizer, model, current_question: str, recent_messages: list[dict] | None = None) -> str:
    """
    Takes conversation history and current message
    in user prompt to rewrite query for retrieval
    """

    if not recent_messages:                # handles both [] and None
        return current_question

    system_prompt = get_system_prompt()
    user_prompt = get_user_prompt(current_question=current_question, recent_messages=recent_messages)

    messages = build_messages(system_prompt=system_prompt, user_prompt=user_prompt)

    retrieval_query = generate_response(tokenizer=tokenizer, model=model, messages=messages)

    return retrieval_query