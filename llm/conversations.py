from config import CONVERSATION_SUMMARY_TURNS


def should_summarize(active_messages: list[dict]) -> bool:
    """
    Checks if summarization of conversation is required,
    returns True or False
    """

    messages = len(active_messages)
    turns = messages // 2

    # return True if condition is satisfied, else False
    return turns >= CONVERSATION_SUMMARY_TURNS


def build_history(summaries: list[dict], active_messages: list[dict]) -> list[dict]:
    """
    Combine and return summaries and current turns
    """

    # returns a new list, .extend() alters list in place, not recommended here.
    return summaries + active_messages



def archive_messages(summaries: list[dict], active_messages: list[dict], summary: str) -> None:
    """
    Creates a dict object for summary and appends it to summaries list,
    Clears existing active_messages list.
    """

    summaries.append(
        {
            "role" : "summary",
            "content" : summary
        }
    )

    active_messages.clear()