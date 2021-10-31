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
  screenshot = ImageGrab.grab()

  img = np.array(screenshot.getdata(), dtype='uint8').reshape((screenshot.size[1],screenshot.size[0],3))

  #rescaled = (255.0 / img.max() * (img - img.min())).astype(np.uint8)

  #im = Image.fromarray(rescaled)
  #im.save('test2.png')

  patt = cv2.imread('butt03.png', 0)#Enter your button
  h,w,points = find_patt(img, patt, 0.60)
  #print(list(points)[0][0]+w/2)
  arr=list(points)
  #print (list(points)[0][1])
  if len(arr)!=0:
    #pyautogui.moveTo(650, 100)
    #print(list(points))
    #print(list(points)[0][1])
    #pyautogui.moveTo(list(points)[0][0]+w/2, list(points)[0][1]+h/2)
    #time.sleep(1)
    #pyautogui.click()
    print(arr[0][0]+w/2, arr[0][1]+h/2)
    #pyautogui.click(x=650, y=700, clicks=3, interval=1)
    pyautogui.click(x=arr[0][0]+w/2, y=arr[0][1]+h/2, clicks=1, interval=1)
    print("finish")