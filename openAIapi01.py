
import openai

openai.api_key = "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"



completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "Hi ChatGPT, you are an ice cream salesperson and marketing major in college."},
    {"role": "user", "content": "Create a name for a new ice cream shop in Fresno, California"}
  ]

)

print(completion.choices[0].message)



print("\n\n Welcome to the OpenAI API Python Program!\n\n")
