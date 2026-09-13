import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()
response = client.responses.create(
    model=os.environ["OPENAI_API_KEY"],
    input="Explain Python virtual environments in one short sentence."
)

print(response.output_text)
