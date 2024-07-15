
import google.generativeai as genai
from google.generativeai import GenerativeModel
import gradio as gr
import os

model = GenerativeModel('gemini-1.5-flash')

os.environ['API_KEY']="your_api_key"
genai.configure(api_key=os.environ['API_KEY'])

def chat(user_input):
    response= model.generate_content(user_input)
    generated_text= response.text
    return generated_text


def main():
    iface= gr.Interface(fn=chat, inputs="text", outputs="text", title="AI CHATBOT by ginni")
    iface.launch(share=True)

if __name__== "__main__":
    main()

    #we did it lessgoo