import os
from dotenv import load_dotenv
import openai

# Load environment variables from the .env file
load_dotenv()

# Set your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Now you can use openai.api_key in your requests



from openai import OpenAI
client = OpenAI()

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a coding assistant, skilled in explaining complex programming concepts to beginers in an instructive way."},
    {"role": "user", "content": "explain the concept of {teacher_one} in programming."}
  ]
)

print(completion.choices[0].message)