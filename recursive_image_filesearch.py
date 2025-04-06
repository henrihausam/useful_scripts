import os

from glob import glob #This is a standard library module so not needed in requirements.txt

from PIL import Image

filename = "example.png"

def get_file(filename: str):
    """ 
    Recursively search for the file from the base directory.
    """
    base = os.path.abspath("C:\\") # Replace with your base directory. I used C:\\ because I had no idea where my file was.
    for file in glob(os.path.join(base, "**", "*"), recursive=True):
        if os.path.basename(file) == filename: #extracts the file name from the path and compares it to the filename
            print(f"Found {filename} at {file}.")
            return file
    return None

def compress_images(imagefile: str, quality=70, max_width=None):
    """
    Compress the image to a specified quality and maximum width.
    """
    image = get_file(imagefile)
    if image is None:
        print(f"File {imagefile} not found.")
        return
    else:
        with Image.open(image) as img: #use with to auto close the file after processing

            if max_width and img.width > max_width:
                ratio = max_width / float(img.width) #calculates the ratio of the new width to the old width to evenly reshape the image in width and height
                new_height = int(img.height * ratio) #calculates the new height using the ratio
                img = img.resize((max_width, new_height), Image.LANCZOS) #LANCZOS is a high-quality downsampling filter found it googling every other could be used but this is the best one

            img.save(image, format="png", optimize=True, quality=quality) #saves the image with the new quality and format. PNG is lossless so it won't lose any quality but it will be smaller in size.
            print(f"Compressed {imagefile} to {quality}% quality.")
            
compress_images(imagefile=filename, quality=70, max_width=500)