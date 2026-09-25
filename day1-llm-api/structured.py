from dotenv import load_dotenv
from google import genai
from google.genai import types
from pydantic import BaseModel

load_dotenv()
client = genai.Client()
MODEL = "gemini-3.5-flash-lite"

class Recipe(BaseModel):
    name: str
    prep_time_minutes: int
    ingredients: list[str]

response = client.models.generate_content(
    model=MODEL,
    contents="Give me a simple recipe for pancakes.",
    config=types.GenerateContentConfig(
        response_mime_type="application/json",
        response_schema=Recipe,
    ),
)
recipe = response.text
print(type(recipe))