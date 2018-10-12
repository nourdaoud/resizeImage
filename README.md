# Resize Images to Square Size
A python script to resize images using Pillow (the PIL fork). It maintains aesthetics by adding black padding to achieve a square size.

Tested with Python version python 2.7.10 and pillow (The PIL fork - version 1.1.7 - to install: $ pip install Pillow)

## Testing Method: 
Run the following : python resize.py path/to/image.ext
Example: python resize.py ./Ousama.png 
(Ousama.png is uploaded with the project - the program expects the extension to be present):

## Expected Output 
The image is turned into a square by padding it and shown. Its dimensions are  displayed in the console. It's also stored under <path/to/image_squared.extension>

## Example:
$ python resize.py ./Ousama.png 
Squared image created by padding the current image - new dimensions: (582,582)
<Image shown>

## Sample output for an image already square:
$ python resize.py ./Ousama_squared.png 
Image is already square - dimensions: (582,582)
