import PIL.Image

# ascii charcters used to build the output text
ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "." ] # this includes charcter in descending order of brightness intensity
    # Each pixel will get associated with one of these characters

# Resize image according to a new width
def resize_image(image, new_width=100):
    width, height = image.size # Gets the width and height of the image 
    ratio = height / width # Calculate a ratio to help in correctly resizing the image
    new_height = int(new_width * ratio) # Create new 
    resize_img = image.resize

def main():
    path = input("Enter a valid pathname to an image")

    try:
        image = PIL.Image.open(path)
    except:
        print(path, 'This is not a valid pathname')