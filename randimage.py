from PIL import Image
import numpy as np
import pyscreenshot as ImageGrab

data = np.random.random((100,100))

#Rescale to 0-255 and convert to uint8
rescaled = (255.0 / data.max() * (data - data.min())).astype(np.uint8)

im = Image.fromarray(rescaled)
im.save('test.png')

screenshot = ImageGrab.grab()
img = np.array(screenshot.getdata(), dtype='uint8').reshape((screenshot.size[1], screenshot.size[0], 3))
rescaled = (255.0 / img.max() * (img - img.min())).astype(np.uint8)

im = Image.fromarray(rescaled)
im.save('test2.png')