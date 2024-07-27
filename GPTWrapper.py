# Authors: Rajeev Choudhari And Benson Tran
# Date: 11/16/2022

# GPTWrapper.py

# This code will call gpt and return the response.

import openai

# Set up your API key
openai.api_key = 'your-api-key-here'

# Define the prompt
prompt = "What is the capital of France?"

# Make the API call
response = openai.Completion.create(
    engine="text-davinci-003",  # You can use other engines as well
    prompt=prompt,
    max_tokens=50  # Adjust the number of tokens as needed
)

# Print the response
print(response.choices[0].text.strip())