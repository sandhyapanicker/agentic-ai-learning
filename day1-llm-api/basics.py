from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
client = genai.Client()
MODEL = "gemini-3.5-flash-lite"

response = client.models.generate_content(
    model=MODEL,
    contents=[
        types.Content(role="user", parts=[types.Part(text="What's the capital of France?")]),
        types.Content(role="model", parts=[types.Part(text="Paris.")]),
        types.Content(role="user", parts=[types.Part(text="What's a good day trip from there?")]),
    ],
    config=types.GenerateContentConfig(
        system_instruction="You are a concise, factual travel assistant. Answer in one or two sentences.",
    ),
)
print(response.text)