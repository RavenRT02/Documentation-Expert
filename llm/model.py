# Initial project is run on google colab's free tier T4 compute.

import os 
from dotenv import load_dotenv
import torch
from huggingface_hub import login
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
from config import MAX_NEW_TOKENS, TEMPERATURE
from llm.prompt import get_system_prompt, get_user_prompt


def login_huggingface(token=None):
    """
    Authenticate with Hugging Face.

    If a token is provided, it is used directly (colab secrets).
    Otherwise, the function attempts to load HF_TOKEN from a local .env file.

    Args: token (str | None): Hugging Face access token.

    Raises: ValueError: If no token is provided or found.
    """

    if token is None:
        load_dotenv()
        token = os.getenv("HF_TOKEN")

    if not token:
        raise ValueError(
            "Hugging Face token not found. "
            "Provide a token or set HF_TOKEN in the .env file. "
            "or import user data from google colab."
        )
    
    login(token=token, add_to_git_credential=False)

    print("Successfully authenticated with Hugging Face")



def load_model(model_name):
    """
    Load a Hugging Face causal language model (predict next likely word ) 
    Quantizing it to 4-bit and tokenizer.

    Args: model_name (str): Hugging Face model identifier.

    Returns: tuple: (tokenizer, model)
    """

    # Trailing comma to support more parameters in future without line edits.
    quantization_config = BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_use_double_quant=True,
        bnb_4bit_compute_dtype=torch.bfloat16,
        bnb_4bit_quant_type="nf4",
    )

    tokenizer = AutoTokenizer.from_pretrained(model_name)

    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    # device_map="auto" - Tells hugging face where to place the model layers.
    # The Transformers library automatically detects available hardware and decides where each layer should go. (GPU or CPU or both)
    # If device_map is not set, it loads the layers onto CPU unless model.to("cuda") is specified somewhere
    model = AutoModelForCausalLM.from_pretrained(model_name, device_map="auto", quantization_config=quantization_config)
    # print(model.hf_device_map) - uncomment to check where the model is placed for testing "{'': 0}" is Cuda 0

    # .eval() one of Pytorch modes used for inference (other is training .train())
    # Some neural network layers behave differently during training and inference. Std practice to use model.eval() for inference.
    model.eval()

    return tokenizer, model

# context is str since the list[Document] will be formatted by other fucntions to provide str
def generate_response(tokenizer, model, question: str, context: str, history: str | None=None, 
                      max_new_tokens=MAX_NEW_TOKENS):
    
    """
    Gets system_prompt and user_prompt to build messages, finds location of model parameters and stores is as device,
    uses apply_chat_template to model tokenizer to create tensor objects that are placed on device,
    model generates output based on inputs and max_new_tokens,
    The output is parsed and the response is returned.
    """
    
    system_prompt = get_system_prompt()
    user_prompt = get_user_prompt(question=question, context=context, history=history)

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ]

    # Every tensor in Pytorch knows where it lives
    # takes the first parameter from the iterated parameters of the model and stores the device to the device variable
    # can be CPU or Cuda:0 or Cuda:1 (Cuda:0 - default GPU, Cuda:1 - additional GPU)
    device = next(model.parameters()).device

    # tokenizer.apply_chat_template takes the messages and modifies it to a structure with additional tokens that 
    # the chosen model can understand and the returned python list is converted to tensors which the model can use directly
    # return_dict=True provides attention_mask and not just input_ids from tokenizer 
    inputs = tokenizer.apply_chat_template(messages, tokenize=True, return_dict=True, 
                                           return_tensors="pt", add_generation_prompt=True)
    
    # Takes k,v in inputs.items(), and turns them into tensor which device can use 
    # k = "input_ids" and v = tensor(...) becomes "input_ids": tensor(...).to(device)
    # k = "attention_mask" and v = "attention_mask": tensor(...).to(device)
    # dict comprehension used so we can unpack the dict in outputs with **inputs
    inputs = {k : v.to(device) for k, v in inputs.items()}


    # torch.inference_mode() is specifically designed for inference.
    # It disables gradient tracking and a few additional bookkeeping operations, making it slightly faster and more memory-efficient.
    with torch.inference_mode():
        # Temperature parameter is not used since do_sample is set to False.
        outputs = model.generate(**inputs, max_new_tokens=max_new_tokens,do_sample=False)

    response = tokenizer.decode(outputs[0][inputs.shape[-1]:], skip_special_tokens=True)

    return response.strip()