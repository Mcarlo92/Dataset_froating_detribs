# Dataset_froating_detribs
This script processes images and their corresponding XML annotations from a specified directory. It performs the following steps:

Import Libraries: Imports necessary libraries including os, numpy, xml.etree.ElementTree, and PIL.Image.

Set Directories: Defines the directories for training data, images, and XML annotations.

List Image Files: Retrieves a list of image file names from the image directory.

Process Each Image: Loops through each image file:

Loads the image.

Converts the image to a numpy array.

Loads the corresponding XML file.

Extracts object information (class name and bounding box coordinates) from the XML file.

Adjusts bounding box size if it is smaller than 200x200 pixels.

Crops the image based on the bounding box coordinates.

Saves the cropped image with a new name.
