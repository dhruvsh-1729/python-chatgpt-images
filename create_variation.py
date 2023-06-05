import os
import openai
from PIL import Image
# openai.organization = "org-yGdAOMPdL7LZAWKNloREPFZJ"
openai.api_key = os.getenv("OPENAI_API_KEY")

image1 = Image.open('sci.png').resize((512,512)).save('sci1.png')

response = openai.Image.create_variation(
  image=open("sci1.png", "rb"),
  n=1,
  size="512x512"
)

image_url = response['data'][0]['url']

print(image_url)