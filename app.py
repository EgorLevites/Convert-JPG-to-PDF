import os
import shutil
from PIL import Image

def convert_and_move_jpg_to_pdf(source_folder, moved_jpg_folder, log_file):
    # Check if the folder for moving JPG files exists, if not, create it
    if not os.path.exists(moved_jpg_folder):
        os.makedirs(moved_jpg_folder)

    # Get a list of all .jpg files in the source folder
    if not os.path.exists(source_folder):
        print(f"Source folder {source_folder} does not exist.")
        return
    
    jpg_files = [f for f in os.listdir(source_folder) if f.lower().endswith('.jpg')]

    for jpg_file in jpg_files:
        # Open the JPG file
        image_path = os.path.join(source_folder, jpg_file)
        try:
            image = Image.open(image_path)
        except Exception as e:
            print(f"Error opening image {image_path}: {e}")
            continue

        # Convert the image to PDF
        pdf_path = os.path.join(source_folder, os.path.splitext(jpg_file)[0] + '.pdf')
        try:
            image.save(pdf_path, "PDF", resolution=100.0)
            print(f"Converted {jpg_file} to {pdf_path}")
        except Exception as e:
            print(f"Error converting {jpg_file} to PDF: {e}")
            image.close()  # Ensure image is closed
            continue

        # Copy the JPG file to the specified folder
        moved_jpg_path = os.path.join(moved_jpg_folder, jpg_file)
        try:
            shutil.copy(image_path, moved_jpg_path)
            print(f"Copied {jpg_file} to {moved_jpg_path}")
        except Exception as e:
            print(f"Error copying {jpg_file} to {moved_jpg_path}: {e}")
            continue

        # Write the file name to the log file (append mode)
        try:
            with open(log_file, 'a') as f:
                f.write(f"{jpg_file}\n")
        except Exception as e:
            print(f"Error writing to log file {log_file}: {e}")
            continue

        # Remove the original JPG file from the source folder
        try:
            os.remove(image_path)
            print(f"Removed original {jpg_file} from {source_folder}")
        except Exception as e:
            print(f"Error removing {jpg_file} from {source_folder}: {e}")

        # Close the image file explicitly
        image.close()

if __name__ == "__main__":
    source_folder = "jpeg_main_files"  # Specify the path to the folder with JPG files
    moved_jpg_folder = "converted_jpeg"  # Specify the path to the folder for moving JPG files
    log_file = "list.txt"  # Specify the path to the log file
    
    convert_and_move_jpg_to_pdf(source_folder, moved_jpg_folder, log_file)
