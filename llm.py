from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from os import getenv

load_dotenv()

BASE_URL = getenv('OPENAI_API_BASE')
API_KEY = getenv('OPENAI_API_KEY')

FAST_MODEL = getenv('FAST_MODEL')
REASONING_MODEL = getenv('REASONING_MODEL')

# GROQ_API_KEY=getenv('GROQ_API_KEY')

fast_llm = ChatOpenAI(
    model=FAST_MODEL,
    base_url=BASE_URL,
    api_key=API_KEY
)

reasoning_llm = ChatGroq(
    model=REASONING_MODEL,
    base_url=BASE_URL,
    api_key=API_KEY
)