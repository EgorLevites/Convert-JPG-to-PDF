
# JPG to PDF Converter

This script converts JPG files to PDF format, moves the original JPG files to a specified folder, and logs the names of the moved files.

## Prerequisites

- Python 3.x
- Pillow library

### Installing the required libraries

```sh
pip install Pillow
```

## Usage

1. **Clone the repository or download the script:**

```sh
git clone <repository_url>
```

2. **Set the paths in the script:**

Edit the `source_folder`, `moved_jpg_folder`, and `log_file` variables in the script with your specific paths.

```python
source_folder = "/path/to/source_folder"  # Specify the path to the folder with JPG files
moved_jpg_folder = "/path/to/moved_jpg_folder"  # Specify the path to the folder for moving JPG files
log_file = "/path/to/log_file.txt"  # Specify the path to the log file
```

3. **Run the script:**

```sh
python convert_and_move_jpg_to_pdf.py
```

## Script Details

The script performs the following tasks:

1. **Check and create folders:**
   - Checks if the folder for moving JPG files exists; if not, creates it.

2. **Convert JPG to PDF:**
   - Converts each JPG file in the source folder to a PDF file.
   - Saves the PDF files in the source folder.

3. **Move the original JPG files:**
   - Copies the original JPG files to the specified folder for moved JPG files.
   - Logs the names of the moved files in the log file (appends to the existing log).

4. **Remove the original JPG files:**
   - Removes the original JPG files from the source folder.

