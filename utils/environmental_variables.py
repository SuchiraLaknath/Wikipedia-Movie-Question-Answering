import os
from dotenv import load_dotenv

load_dotenv()


def get_variable(id:str):
    return os.environ.get(id)

def get_groq_api_key(id="GROQ_API_KEY"):
    return get_variable(id= id)
