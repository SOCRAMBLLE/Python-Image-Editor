# Image Editor and Converter

Welcome to the Image Editor and Converter project! This Python script allows you to apply filters, enhance contrast, and convert images from JPG to WebP format. Follow the instructions below to use the scripts.

## Filters and Contrast Enhance
The photoEdit.py script applies filters and enhances contrast to the images in the images folder. Feel free to modify the script to customize the filters and enhance settings to your preference.

## JPG to WebP Conversion
The JPGtoWebP.py script converts JPG images to WebP format. WebP is a modern image format that offers smaller file sizes while maintaining quality. The converted images are saved in the convertedImgs folder.


## Prerequisites

Before you begin, make sure you have the following installed:

- [Python](https://www.python.org/downloads/) - The programming language.
- [Pillow](https://pillow.readthedocs.io/en/stable/installation.html) - The Python Imaging Library (PIL), used for image processing.

## Installation

1. Clone this repository to your local environment:
```bash
git clone https://github.com/YOUR_USERNAME/REPO_NAME.git
cd REPO_NAME
```

2. Install the required dependencies using pip:
```bash
py -m pip install --upgrade Pillow
```

## Usage

### Image Editing

1. Place your original images in the "images" folder.
2. Run the script to apply filters and contrast enhancement and save edited images to the "editedImgs" folder:
```bash
py photoEdit.py
```
3. Check the "editedImgs" folder for the edited images.

### Image Conversion (JPG to WebP)

1. Place the images you want to convert in the images folder.
2. Run the script to convert images from JPG to WebP:
```bash	
python JPGtoWebP.py
```
3. Converted images will be saved in the convertedImgs folder.



## Contribution
Contributions are welcome! If you'd like to contribute to this project, follow these steps:

1. Fork the repository.
2. Create a new branch: git checkout -b feature/your-feature
3. Make your changes and commit them.
4. Push the changes to your fork: git push origin feature/your-feature
5.  Create a pull request.
