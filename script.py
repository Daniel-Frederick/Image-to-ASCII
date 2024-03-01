# Used this website to help create and understand PIL.Image library 
# https://pillow.readthedocs.io/en/stable/reference/Image.html
import PIL.Image

# ascii characters used to build the output text
ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", "," ] # This includes charcter in descending order of brightness intensity
# Each pixel will get associated with one of these characters

# 1. Resize image according to a new width
def resize_image(image, new_width=100):
    width, height = image.size # Gets the width and height of the image
    ratio = height / width / 1.65 # Calculate a ratio to help in correctly resizing the image
    new_height = int(new_width * ratio) # Calculate the new height of the image
    resized_image = image.resize((new_width, new_height)) # Pass a tuple that represents the new image size
    return(resized_image) # Get the newly resized image

# 2. Convert the image to grayscale
def grayscale_image(image):
    grayscale_image = image.convert("L") # Removes color information from the image to vonert to grayscale
    return(grayscale_image) # Return the new image

# 3. Convert pixels to a String of ASCII Characters
def asciiConverter(image):
    pixels = image.getdata() # Returns a list of each pixels grayscale value
    # Determine the scaling factor to fit the grayscale values within the range of ASCII_CHARS
    scaling_factor = 255 / (len(ASCII_CHARS) - 1)
    # Map the grayscale values to ASCII characters, by iterating through each pixel and assign it an ASCII character
    characters = "".join([ASCII_CHARS[int(pixel / scaling_factor)] for pixel in pixels])
    return characters

def main(new_width=100):
    # Ask user to enter a valid pathname to an image
    path = input("Enter an absolute pathname to an image in your File Explorer:\n")
    pathList = path.split("\\") # Split the pathname into each directory name
    # print(pathList)
    pathname = pathList[len(pathList)-1] # Get the filename of the image entered
    pathname = pathname[:-4] # Remove .xxx from the end of the filename
    # print(pathname)

    # Error handling to make sure that the the filename is correct
    try:
        # If the image is correct then get that image
        image = PIL.Image.open(path)
        print(image, "  is a good image")

        resize_image = resize_image(image)
        print("resize works")

        gray = grayscale_image(resize_image)
        print("grayify works")
        
        # convert image to ascii    
        new_image_data = asciiConverter(gray)
        print("asciiConverter  works")

        # # Resize the image, convert to grayscale, then convert to ASCII
        # new_image = asciiConverter(grayscale_image(resize_image(image)))
        # print(new_image, "  is a good image")
        
        # Image not yet formatted in aspect ratio
        # Formatting the ASCII characters
        pixel_count = len(new_image_data) # Get image length
        # Add an indent whenever the pixel_length is met
        ascii_image = "\n".join([new_image_data[index:(index+new_width)] for index in range(0, pixel_count, new_width)])
        
        # print image in terminal
        # print(ascii_image)
        
        # Save image to your files
        # save result to pathname + ".txt"
        with open(pathname + ".txt", "w") as f:
            f.write(ascii_image)
            print("Your new text file named:" + pathname + ".txt")


    except:
        print(path, " is not a valid pathname to an image.")
        
 
# run program
main()