# https://www.youtube.com/watch?v=v_raWlX7tZY&ab_channel=Kite
# Used this website to help create and understand Image library 
# https://pillow.readthedocs.io/en/stable/reference/Image.html
import PIL.Image

# ascii charcters used to build the output text
ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "." ] # this includes charcter in descending order of brightness intensity
    # Each pixel will get associated with one of these characters

# Resize image according to a new width
def resize_image(image, new_width=100):
    width, height = image.size # Gets the width and height of the image 
    ratio = height / width / 1.65 # Calculate a ratio to help in correctly resizing the image
    new_height = int(new_width * ratio) # Calculate the new height of the image 
    resized_image = image.resize((new_width, new_height)) # Pass a tuple that represents the new image size
    return resize_image # Get the newly resized image

# Convert the image to grayscale
def grayscale_image(image):
    grayscale_image = image.convert("L") # Removes color information from the image
    return grayscale_image # Return the new image

# Convert pixels to a String of ASCII Characters
def asciiConverter(image): 
    pixels = image.getdata() # 

def main():
    path = input("Enter a valid pathname to an image")

    try:
        image = PIL.Image.open(path)
    except:
        print(path, 'This is not a valid pathname')