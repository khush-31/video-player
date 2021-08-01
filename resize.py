import cv2
import os

def reducesize(path):
    img=cv2.imread(path,1)
    img=cv2.resize(img,(1280,480))
    cv2.imwrite(path,img)
fileList = []
dirpath ='rec'
for f in os.listdir(dirpath):
    fpath = os.path.join(dirpath, f)
    if os.path.isfile(fpath) and f.endswith(('.png', '.jpg', '.jpeg')):
        reducesize(fpath)

