from openai import OpenAI
from PIL import Image
import streamlit as st
from apikey import apikey

#Initialize image generalized client
client= OpenAI(api_key=apikey)

def generate_images(image_description, num_images):
    img_response= client.images.generate(
        model= "dall-e-3",
        prompt= image_description,
        size='1024x1024',
        quality='standard',
        n=1

    )
    image_url= img_response.data[0].url
    return image_url

st.set_page_config(page_title="Image-Geneartion", page_icon=":camera", layout="wide")

#image generation title
st.title("Image-Generation")

#create subheader
st.subheader("Powered by most Powerful image generation APP")

img_description= st.text_input("Enter a description for the image ")
num_of_images= st.number_input("Select the number of images you want to generate", min_value= 1, max_value= 5, value= 1)

#create button 
if st.button("Generate image"):
    generate_image= generate_images(img_description, num_of_images)

    
    st.image(generate_image)
