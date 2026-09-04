import os
from dotenv import load_dotenv
from openai import OpenAI
from llm.model import load_model, generate_response
from config import LLM_PROVIDER, LLM_MODEL, LLM_BASE_URL



class LocalLLM:
    """
    Wrapper around the local Hugging Face model.

    The underlying model and tokenizer are loaded once and reused
    for query rewriting and response generation.
    """

    def __init__(self, model_name: str):
        """
        Load tokenizer and model
        """

        # In case of using a gated/private model instead of qwen and similar models, 
        # login_huggingface() can be imported from llm/models and used here replacing this line for login.
        self.tokenizer, self.model = load_model(model_name=model_name)

    def generate(self, messages: list[dict]) -> str:
        """
        Generate response using HF model
        """

        return generate_response(tokenizer=self.tokenizer, model=self.model, messages=messages)


class APIClient():
    """
    Client for OpenAI-compatible chat completions APIs
    """

    def __init__(self, model_name: str, api_key: str, base_url: str | None = None):

        self.model_name = model_name
        self.client = OpenAI(api_key=api_key, base_url=base_url)


    def generate(self, messages: list[dict]) -> str:
        """
        Generate response using the configured model
        """

        response = self.client.chat.completions.create(model=self.model_name, messages=messages)

        return response.choices[0].message.content.strip()



def load_llm():
    """
    Loads the configured LLM backend
    Returns : LocalLLM or APIClient depending on the LLM_PROVIDER
    """

    if LLM_PROVIDER == "local":
        return LocalLLM(model_name=LLM_MODEL)

    if LLM_PROVIDER == "api":

        load_dotenv()
        api_key = os.getenv("LLM_API_KEY")

        if not api_key:
            raise ValueError("API key not found. Set LLM_API_KEY in .env file.")

        return APIClient(model_name=LLM_MODEL, api_key=api_key, base_url=LLM_BASE_URL)

    raise ValueError(f'Unsipported LLM provider: {LLM_PROVIDER}')