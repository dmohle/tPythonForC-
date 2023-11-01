import openai

# Replace 'your-api-key' with your actual OpenAI API key
openai.api_key = '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'

# Choose the model you wish to use (as of my last update, "text-davinci-003" was a powerful model)
# You might want to check if there's a newer model available.
model_name = "gpt-3.5-turbo"

# Create a prompt that you want the AI to respond to
prompt = "Say hello to my C++ Class and tell them a funny programming joke."

# Make a request to the API
response = openai.Completion.create(
  model=model_name,
  prompt=prompt,
  temperature=0.7,
  max_tokens=60
)

# Print the text response
print(response.choices[0].text.strip())