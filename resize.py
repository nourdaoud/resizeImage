#Using Pillow, the (currently - 10/06) maintained PIL library
#https://pillow.readthedocs.io/en/3.1.x/reference/Image.html 
from PIL import Image

#You can specify the mode e.g. 'L' will make it black and white
def square_image (image, mode='RGBA',  min_size = 100, color = 'black'):
	x,y = image.size
	size = max(min_size, x, y)
	squared = Image.new(mode , (size, size), color)
	#The tuple specifies the top left corner where the original image will be pasted 
	squared.paste(image, ((size - x)/2, (size-y)/2))
	return squared

#uncomment to test
#test=Image.open("./Ousama.png")
#squared=square_image(test)
#squared.show() 
