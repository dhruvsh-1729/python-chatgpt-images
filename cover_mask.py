import os
import openai
from PIL import Image
# openai.organization = "org-yGdAOMPdL7LZAWKNloREPFZJ"
openai.api_key = os.getenv("OPENAI_API_KEY")

image1 = Image.open('goi.png').resize((512,512)).convert('RGBA').save('goi1.png')
image2 = Image.open('mask.png').resize((512,512)).convert('RGBA').save('mask1.png')

response = openai.Image.create_edit(
  image=open("goi1.png", "rb"),
  mask=open("mask1.png", "rb"),
  prompt="Sunlit monumental area with lots of birds",
  n=1,
  size="512x512"
)
image_url = response['data'][0]['url']
print(image_url)