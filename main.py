import os, sys
from dotenv import load_dotenv
from google import genai

# Load environment variables from .env file
load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

# Initialize the Gemini client
client = genai.Client(api_key=api_key)

# Check if command line argument is provided
if len(sys.argv) != 2:
    print('Usage: python3 main.py "Input text"')
    sys.exit(1) # Exit if no input text is provided
    
response = client.models.generate_content(model="gemini-2.0-flash-001", contents=sys.argv[1])
print(response.text)
print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
