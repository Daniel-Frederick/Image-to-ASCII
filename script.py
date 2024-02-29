# # https://www.youtube.com/watch?v=v_raWlX7tZY&ab_channel=Kite
# # Used this website to help create and understand Image library 
# # https://pillow.readthedocs.io/en/stable/reference/Image.html
# import PIL.Image
# from PIL import Image

# # ascii charcters used to build the output text
# ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", "," ] # this includes charcter in descending order of brightness intensity
#     # Each pixel will get associated with one of these characters

# # 1. Resize image according to a new width
# def resize_image(image, new_width=100): 
#     width, height = image.size # Gets the width and height of the image 
#     ratio = height / width / 1.65 # Calculate a ratio to help in correctly resizing the image
#     new_height = int(new_width * ratio) # Calculate the new height of the image 
#     resized_image = image.resize((new_width, new_height)) # Pass a tuple that represents the new image size
#     return (resized_image) # Get the newly resized image

# # 2. Convert the image to grayscale
# def grayscale_image(image): 
#     grayscale_image = image.convert("L") # Removes color information from the image to vonert to grayscale
#     return (grayscale_image) # Return the new image

# # 3. Convert pixels to a String of ASCII Characters
# def asciiConverter(image): 
#     pixels = image.getdata() # Returns a list of each pixels grayscale value
#     # Using a list, iterate through each pixel and assign it an ASCII character
#     characters = "".join([ASCII_CHARS[pixel // 25] for pixel in pixels])
#     return (characters)

# def main(new_width = 100):
#     # Ask user to enter a valid pathname to an image
#     path = input("Enter a valid pathname to an image: \n")

#     # Error handling to make sure that the the filename is correct
#     try:
#         # If the image is correct then get that image
#         image = PIL.Image.open(path)

#         print(image, "  is a good image")
        
#         # Resize the image, convert to grayscale, then convert to ASCII
#         new_image = asciiConverter(grayscale_image(resize_image(image)))
#         print(new_image, "  is a good image")


#         # Image not yet formatted in aspect ratio
#         # Formatting the ASCII characters
#         pixel_length = len(new_image) # Get image length
#         # Add an indent whenever the pixel_length is met
#         ascii_image = "\n".join(new_image[i:(i + new_width)] for i in range(0, pixel_length))

#         # Print image
#         # print(ascii_image)
#         print("Made it to print(ascii_image) ")

#         # Save image to your files
#         with open("ascii_image.txt", "w") as f: # New file will have name "ascii_image.txt"
#             f.write(ascii_image)



#     except:
#         # If the file does not lead to an image, tell the user
#         print(path, 'This is not a valid pathname')

#     # # Resize the image, convert to grayscale, then convert to ASCII
#     # new_image = asciiConverter(grayscale_image(resize_image(image)))

#     # # Image not yet formatted in aspect ratio
#     # # Formatting the ASCII characters
#     # pixel_length = len(new_image) # Get image length
#     # # Add an indent whenever the pixel_length is met
#     # ascii_image = "\n".join(new_image[i:(i + new_width)] for i in range(0, pixel_length))

#     # # Print image
#     # print(ascii_image)

#     # # Save image to your files
#     # with open("ascii_image.txt", "w") as f: # New file will have name "ascii_image.txt"
#     #     f.write(ascii_image)

# main()

import PIL
import PIL.Image
from PIL import Image

# ascii characters used to build the output text
ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

# resize image according to a new width
def resize_image(image, new_width=100):
    width, height = image.size
    ratio = height/width
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return(resized_image)

# convert each pixel to grayscale
def grayify(image):
    grayscale_image = image.convert("L")
    return(grayscale_image)
    
# convert pixels to a string of ascii characters
# def pixels_to_ascii(image):
#     pixels = image.getdata()
#     characters = "".join([ASCII_CHARS[pixel//25] for pixel in pixels])
#     return(characters)  

def pixels_to_ascii(image):
    pixels = image.getdata()
    # Determine the scaling factor to fit the grayscale values within the range of ASCII_CHARS
    scaling_factor = 255 / (len(ASCII_CHARS) - 1)
    # Map the grayscale values to ASCII characters
    characters = "".join([ASCII_CHARS[int(pixel / scaling_factor)] for pixel in pixels])
    return characters



def main(new_width=100):
    # attempt to open image from user-input
    path = input("Enter a valid pathname to an image:\n")
    pathList = path.split("\\")
    print(pathList)
    pathname = pathList[len(pathList)-1]
    pathname = pathname[:-4]
    print(pathname)
    try:
        image = PIL.Image.open(path)
        print(image, "  is a good image")

        resize = resize_image(image)
        print("resize works")

        gray = grayify(resize)
        print("grayify works")
        

        # convert image to ascii    
        new_image_data = pixels_to_ascii(gray)
        print("pixels_to_ascii  works")

        
        # format
        pixel_count = len(new_image_data)  
        ascii_image = "\n".join([new_image_data[index:(index+new_width)] for index in range(0, pixel_count, new_width)])
        
        # print result
        print(ascii_image)
        
        # save result to "ascii_image.txt"
        with open(pathname + ".txt", "w") as f:
            f.write(ascii_image)


    except:
        print(path, " is not a valid pathname to an image.")
        
 
# run program
main()