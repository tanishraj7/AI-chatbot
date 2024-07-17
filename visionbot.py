import google.generativeai as genai
from google.generativeai import GenerativeModel
import os

os.environ['API_KEY']= "your_api_key"
genai.configure(api_key=os.environ['API_KEY'])
#now importing image
import PIL.Image

sample_file1= PIL.Image.open('jetpack.jpg')
sample_file2= PIL.Image.open('piranha.jpg')
sample_file3= PIL.Image.open('firefighter.jpg')

model= GenerativeModel(model_name='gemini-1.5-flash')

promt= "what do you see in all the 3 uploaded images"
response= model.generate_content([promt, sample_file1, sample_file2, sample_file3])

print(">"+ response.text)