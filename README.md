# Dataset_froating_detribs

This script processes images and their corresponding XML annotations from a specified directory. It performs the following steps:

1. **Import Libraries**: Imports necessary libraries including `os`, `numpy`, `xml.etree.ElementTree`, and `PIL.Image`.
2. **Set Directories**: Defines the directories for training data, images, and XML annotations.
3. **List Image Files**: Retrieves a list of image file names from the image directory.
4. **Process Each Image**: Loops through each image file:
   - Loads the image.
   - Converts the image to a numpy array.
   - Loads the corresponding XML file.
   - Extracts object information (class name and bounding box coordinates) from the XML file.
   - Adjusts bounding box size if it is smaller than 200x200 pixels.
   - Crops the image based on the bounding box coordinates.
   - Saves the cropped image with a new name.

This script is useful for preparing image datasets with annotations for training machine learning models.

## Requirements
- Python 3.x
- Libraries: `os`, `numpy`, `xml.etree.ElementTree`, `PIL`

## Execution
To run the script, make sure you have the directories `./training/images` and `./training/annotations` with the image files and corresponding XML files. Then, run the script with Python.

```bash
python imgbbox.py
****
