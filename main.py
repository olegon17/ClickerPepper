import cv2
import time
import numpy as np
import pyscreenshot as ImageGrab
import pyautogui
#from PIL import Image

def find_patt(image, patt, thres):
  img_grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  (patt_H, patt_W) = patt.shape[:2]
  res = cv2.matchTemplate(img_grey, patt, cv2.TM_CCOEFF_NORMED)
  #print (res)
  loc = np.where(res>thres)
  #print (loc)
  return patt_H, patt_W, zip(*loc[::-1])


if __name__ == '__main__':
  #animals=('animal.png','animal02.png','animal03.png','animal04.png','animal05.png','animal06.png')
  animals = ('animal.png', 'animal02.png', 'animal05.png')
  while(True):
    screenshot = ImageGrab.grab()
    img = np.array(screenshot.getdata(), dtype='uint8').reshape((screenshot.size[1],screenshot.size[0],3))
    for animal in animals:
      patt = cv2.imread(animal, 0)#Enter your button
      h,w,points = find_patt(img, patt, 0.60)
      arr=list(points)
      if len(arr)!=0:
        print(arr[0][0]+w/2, arr[0][1]+h/2)
        pyautogui.click(x=arr[0][0]+w/2, y=arr[0][1]+h/2, clicks=1, interval=1)
        print("Олень найден!")
        print(animal)
        break
      else:
        continue
    print("Олень не найден")
    time.sleep(1)
  print("finish")