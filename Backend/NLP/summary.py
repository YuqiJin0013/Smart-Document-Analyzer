import openai
import os

def summarize_text_gpt3(client, text):
    """
    Summarizes the given text using the OpenAI GPT-3 model.

    Parameters:
    - client (OpenAI): An instance of the OpenAI client.
    - text (str): The text to summarize.

    Returns:
    - str: The summary of the text, or an error message if an API call fails.
    """
    MODEL = "text-davinci-003"
    try:
        response = client.Completion.create(
            engine=MODEL,
            prompt=f"Summarize the following text:\n{text}",
            max_tokens=150,
        )

        summary = response.choices[0].text.strip()
        return summary
    except openai.OpenAIError as e:
        # Handle specific OpenAI API errors here
        # Log the error for debugging purposes if necessary
        return "Error occurred while summarizing the text"
