import openai

# Initialize the OpenAI API with your API key
openai.api_key = ''

# Function to suggest actions based on a keyword using GPT
def suggest_action(keyword, context):
    # Construct the prompt for the chat model
    prompt = f"The text mentions {keyword}. Based on the context: '{context}', what action should be taken?"

    # Make a request to the GPT model using the new interface
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # You can also use "gpt-4" if available
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=20,  # Adjust based on the length of the action description you want
        temperature=0.7  # Adjust for more creative or deterministic outputs
    )

    # Return the text response
    return response.choices[0].message['content'].strip()

# Example usage
keyword = "rust"
context = "The left front tire of the CAT 730 truck shows significant rust and low pressure."
action = suggest_action(keyword, context)
print(f"Suggested Action for '{keyword}': {action}")
