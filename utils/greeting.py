from utils.formatter import normalize
from config import CONVERSATION_STARTERS, CONVERSATION_CONCLUDERS

def is_greeting(question: str) -> str:
    """
    Checks if the given question is a greeting
    """
    
    normalized_question = normalize(question=question)

    starter_list = CONVERSATION_STARTERS
    concluder_list = CONVERSATION_CONCLUDERS
        
    if normalized_question in starter_list:
        return "starter"
    elif normalized_question in concluder_list:
        return "concluder"
    else:
        return "llm"
    


def handle_greeting(question: str) -> dict:
    """
    wrapper for handling greetings
    """

    greeting_type = is_greeting(question=question)

    if greeting_type == "starter":
    
        starter = {
            "response" : "Hello! What would you like to know about Python, Pandas, or LangChain today?",
            "documents" : []
        }

        return starter

    elif greeting_type == "concluder":

        concluder =  {
            "response" : "You're welcome! Feel free to ask if you have another question about Python, Pandas, or LangChain.",
            "documents" : []
        }

        return concluder
    
    else:
        None