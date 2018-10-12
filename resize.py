#Using Pillow, the (currently - 10/06) maintained PIL library
#https://pillow.readthedocs.io/en/3.1.x/reference/Image.html 
from PIL import Image
import sys
import os 

def main():
	if (len(sys.argv) != 2):
		print 'Usage: ./resize.py <image path>'
		exit()
	square_image(Image.open(sys.argv[1]))

#You can specify the mode e.g. 'L' will make it black and white
#mode and color can be exposed in later versions in main function 
def square_image (image, mode='RGBA',  color = 'black'):
	x,y = image.size
	if (x == y):
		print ('Image is already square - dimensions: ' + int_tup_to_str(image.size))	
		exit()
	size = max(x, y)
	squared = Image.new(mode , (size, size), color)
	#The tuple specifies the top left corner where the original image will be pasted 
	squared.paste(image, ((size - x)/2, (size-y)/2))
	squared.show()
	print ('Squared image created by padding the current image - new dimensions: ' + int_tup_to_str(squared.size))
	save_image(squared)
	return squared

def int_tup_to_str(tup):
	return '(' + ','.join(str(dim) for dim in tup) + ')'
	
def save_image (squared):
	file_name = sys.argv[1]
	image_file_name, ext = sep_extension (file_name)
        squared_image_file_name = image_file_name + '_squared'
	squared.save(squared_image_file_name, ext)
	print 'square image saved under ' + squared_image_file_name + '.' + ext  

def sep_extension(file_name):
	file_name, ext = os.path.splitext(file_name)
	ext = ext.split('.')[1]
	return file_name, ext

if __name__ == "__main__":
	main()

