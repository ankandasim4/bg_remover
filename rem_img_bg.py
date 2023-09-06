import os
from rembg import remove
from PIL import Image

# Specify the source and output directories
source_folder = "static/"
output_folder = "static/"

# Ensure the output folder exists
os.makedirs(output_folder, exist_ok=True)

# List all files in the source folder
for filename in os.listdir(source_folder):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        # Construct the input and output file paths
        input_path = os.path.join(source_folder, filename)
        output_path = os.path.join(output_folder, filename.replace(".jpg", ".png").replace(".png", ".png"))

        # Open the input image using Pillow (PIL)
        with Image.open(input_path) as img:
            # Remove the background and save the result
            output_img = remove(img)
            output_img.save(output_path, "PNG")
            print(f"Processed: {input_path} -> {output_path}")
