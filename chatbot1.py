import os
import google.generativeai as genai

os.environ['API_KEY']="your_api_key"

# Access your API key as an environment variable.
genai.configure(api_key=os.environ['API_KEY'])

model = genai.GenerativeModel('gemini-1.5-flash')

prompt = "Write a 50 words essay on AI."

response = model.generate_content(prompt)

print(response.text)