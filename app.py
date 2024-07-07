import os
from PIL import Image

def convert_and_move_jpg_to_pdf(source_folder, destination_folder, moved_jpg_folder, log_file):
    # Check if the destination folder exists, if not, create it
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # Check if the folder for moving JPG files exists, if not, create it
    if not os.path.exists(moved_jpg_folder):
        os.makedirs(moved_jpg_folder)

    # Create or clear the log file
    with open(log_file, 'w') as f:
        f.write("List of moved JPG files:\n")

    # Get a list of all .jpg files in the source folder
    jpg_files = [f for f in os.listdir(source_folder) if f.lower().endswith('.jpg')]

    for jpg_file in jpg_files:
        # Open the JPG file
        image_path = os.path.join(source_folder, jpg_file)
        image = Image.open(image_path)

        # Convert the image to PDF
        pdf_path = os.path.join(destination_folder, os.path.splitext(jpg_file)[0] + '.pdf')
        image.save(pdf_path, "PDF", resolution=100.0)
        print(f"Converted {jpg_file} to {pdf_path}")

        # Move the JPG file to the specified folder
        moved_jpg_path = os.path.join(moved_jpg_folder, jpg_file)
        os.rename(image_path, moved_jpg_path)
        print(f"Moved {jpg_file} to {moved_jpg_path}")

        # Write the file name to the log file
        with open(log_file, 'a') as f:
            f.write(f"{jpg_file}\n")

if __name__ == "__main__":
    
    source_folder = "/Users/egorlevites/Desktop/Renium/jpeg_main_files"  # Specify the path to the folder with JPG files
    destination_folder = "/Users/egorlevites/Desktop/Renium/pdf_files"  # Specify the path to the destination folder
    moved_jpg_folder = "/Users/egorlevites/Desktop/Renium/converted_jpeg"  # Specify the path to the folder for moving JPG files
    log_file = "/Users/egorlevites/Desktop/Renium/converted_jpeg/list.txt"  # Specify the path to the log file
    
    convert_and_move_jpg_to_pdf(source_folder, destination_folder, moved_jpg_folder, log_file)
