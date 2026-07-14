from utils.formatter import format_history


def build_conversation_summary_prompt(active_messages):
    
    system_prompt = f"""
    INSTRUCTIONS :

    You are a conversation summarizer.
    You will recieve a conversation containing alternating user questions and assistant responses.
    Your task is to summarize the contents a clear and concise manner.
    The resulting summary should not lose the meaning of the conversation.
    Preserve important questions.
    Preserve unsolved questions.
    Preserve user preferences relevant to this session.
    Omit greetings and small talk.
    Do not invent information, do no predict or fill missing information.
    Respond only with conversation summary.

    Converstation list :
    {format_history(active_messages)}
    """

    return system_prompt