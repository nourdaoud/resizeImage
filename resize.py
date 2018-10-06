#Using Pillow, the (currently - 10/06) maintained PIL library
#https://pillow.readthedocs.io/en/3.1.x/reference/Image.html 
from PIL import Image
import sys

def main():
	if (len(sys.argv) != 2):
		print 'Usage: ./resize.py <image path>'
		exit()
	square_image(Image.open(sys.argv[1]))

#You can specify the mode e.g. 'L' will make it black and white
#mode and color can be exposed in later versions in main function 
def square_image (image, mode='RGBA',  color = 'black'):
	x,y = image.size
	size = max(x, y)
	squared = Image.new(mode , (size, size), color)
	#The tuple specifies the top left corner where the original image will be pasted 
	squared.paste(image, ((size - x)/2, (size-y)/2))
	squared.show()
	return squared

if __name__ == "__main__":
	main()

