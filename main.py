import sys
import os
from google import genai
from google.genai import types
from dotenv import load_dotenv


def main():
    load_dotenv()

    args = sys.argv[1:]
    # Check if the user provided a prompt
    # If not, print usage instructions and exit with 1
    if not args:
        print("AI Code Assistant")
        print('\nUsage: python main.py "your prompt here"')
        print('Example: python main.py "How do I build a calculator app?"')
        sys.exit(1)
    verbose = False
    if args[-1] == "--verbose":
        verbose = True
        args.pop()
    # Join the arguments to form the user prompt as a single string
    user_prompt = " ".join(args)
    # Initialize the Google GenAI client
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    generate_content(client, messages, verbose)

# Function to generate content using the Google GenAI client
# It takes the client and a list of messages as input
# and prints the response text
def generate_content(client, messages, verbose):
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
    )
    print("Response:")
    print(response.text)
    if verbose:
        print(f"User prompt: {" ".join(sys.argv[1:])}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")


if __name__ == "__main__":
    main()
