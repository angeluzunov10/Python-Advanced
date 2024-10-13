import tkinter as tk
import json
import urllib.request
import requests

from io import BytesIO
from PIL import ImageTk, Image


def display_image(image_url):
    with urllib.request.urlopen(image_url) as url:
        image_data = url.read()     # download the image

    image_stream = BytesIO(image_data)

    image = ImageTk.PhotoImage(Image.open(image_stream))    # this is the image as Tkinter object

    image_label.config(image=image)    # set the image label
    imae_label.image = image   # keeps reference to the image


def get_image_url():

    headers = {
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiMTQ0OWNiZTYtND"
                         "I4OS00MWQ5LTkzOTQtNTk3MGU3Y2IyMTk0IiwidHlwZSI6ImFwaV90b2tlbiJ9.G5xkrd"
                         "8wVzQrAuYIfLoS2gG8jVWhFisGxeywbt6E85I"}
    # this is the personal key, provided by Eden AI

    url = "https://api.edenai.run/v2/image/generation"
    payload = {
        "providers": "openai",
        "text": input_field.get(),  # bringing the text from the input field and gives it here as a string
        "resolution": "256x256",  # this is the resolution of the image
        "fallback_providers": ""  # in case openai will not work here are the other platforms that can do it
    }

    response = requests.post(url, json=payload, headers=headers)  # post request for what image we want to generate
    result = json.loads(response.text)  # gets response from server and returns result as a dictionary

    return result['openai']['items'][0]['image_resource_url']  # gets link to image resource


def render_image():
    try:
        error_label.place_forget()  # this will remove the label of the error after entering new message
        image_url = get_image_url()
    except KeyError:
        error_label.place(x=175, y=50)
    else:
        display_image(image_url)    # this will visualize the image


window = tk.Tk()
window.title("AI Image Generator")  # title of the main window
window.geometry("500x350")  # width x height of the main window

error_label = tk.Label(window, text="Prompt cannot be empty!", fg="red")
# error label for the main window where if the prompt is empty then it will print text in red color
# if I want background color then I set it with the bg="color"

input_field = tk.Entry(window, width=24)    # in which window is going to be the input field and its width
input_field.place(x=165, y=20)  # on which place is going to be the top left corner of the input field

image_label = tk.Label(window)  # making a label on the main window
image_label.place(x=125, y=70)

generate_button = tk.Button(window, text="Create", height=1, command=render_image)  # button for creating
# in command is a reference to the function, because we want to run the function when the button is clicked

generate_button.place(x=320, y=17)  # on which place is going to be the top left corner of the generate button

window.mainloop()   # this will keep the window open until it is closed
