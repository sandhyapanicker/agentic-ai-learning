from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
client = genai.Client()
MODEL = "gemini-3.5-flash-lite"
for temp in [0.0, 1.0, 2.0]:
    response = client.models.generate_content(
        model=MODEL,
        contents="Suggest a name for a new coffee shop.",
        config=types.GenerateContentConfig(temperature=temp),
    )
    print(f"temp={temp}: {response.text.strip()}")