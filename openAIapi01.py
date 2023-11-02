import openai

openai.api_key = "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"

messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Translate the following English text to French: 'Hello, how are you?'"},
]
temperature = 0.7  # Set the temperature here

completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=messages,
    temperature=temperature
)

print(completion.choices[0].message["content"])
