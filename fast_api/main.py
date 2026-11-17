from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
client = genai.Client()

app = FastAPI()

@app.get("/")
def read_root():
    return {"Message  ": "Welcome"}

@app.get("/margin")
def margin(revenue: float, expenses: float):
    profit  = revenue - expenses
    margin_percent= (profit/revenue)*100
    return {"profit" : profit, "margin-percent": margin_percent }


class Review(BaseModel):
    text:str

class Sentiment(BaseModel):
    label:str
    score:int


@app.post("/sentiment")
def analyze_sentiment(review: Review):
    response = client.models.generate_content(
        model = "gemini-3.5-flash",
        contents=(
            "Find the sentiment of this customer review. "
            "label must be 'postive' , 'negative' , or 'neutral' ."
            "score must be a number from 1 (very bad) to 5 (very good). "
            f"Review: {review.text}"
        ),
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
            response_schema=Sentiment,
        ),
    )

    return response.parsed
