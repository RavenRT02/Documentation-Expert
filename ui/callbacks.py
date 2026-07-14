def chat(pipeline, question, libraries, chat_history):
    """
    Builds chat history for chatbox output
    """

    # Return existing chat_history if user submits empty question
    # Since it returns, pipeline is not called. 
    # "" is returned to reset user_input field after button is clicked
    if not question.strip():
        return chat_history, chat_history, ""

    # call rag pipeline and store just the response key's value of returned dict from ask()
    result = pipeline.ask(question=question, libraries=libraries)
    assistant_response = result["response"]

    # Add user question to chat_history, chat_history is completely for UI no relation with backend
    chat_history.append(
        {
            "role" : "user",
            "content" : question
        }
    )

    # Add llm response to chat_history
    chat_history.append(
        {
            "role" : "assistant",
            "content" : assistant_response
        }
    )

    # return chat_history twice for chatbox, chat_history outputs
    return chat_history, chat_history, ""



def clear_chat(pipeline, chat_history):
    """
    Clear backend and frontend conversation_history
    """

    pipeline.reset_conversation()
    chat_history.clear()
    return chat_history, chat_history, ""