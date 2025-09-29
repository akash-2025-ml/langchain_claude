from prompt import Refined_Prompt_1
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema import SystemMessage, HumanMessage

from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
from typing import Dict

from dotenv import load_dotenv
import os

load_dotenv()


class InputStrings(BaseModel):
    signals: Dict
    classification: str


app = FastAPI()


@app.post("/predict")
def predict(data: InputStrings):
    API_KEY = os.getenv("API_KEY")
    # Initialize LLM with API key
    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash", temperature=0, api_key=API_KEY
    )

    s = """This my 68 sinals {0} with classification labe is {1} . """.format(
        data.signals, data.classification
    )

    # System and user messages
    system_message = SystemMessage(content=Refined_Prompt_1)
    human_message = HumanMessage(content=s)
    response = llm([system_message, human_message])
    return {"output": response.content}
