


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