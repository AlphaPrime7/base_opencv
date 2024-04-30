from zipfile import *
import cv2 as cv

def show_images(zfile):
    from zipfile import ZipFile
    from PIL import Image

    zf_class = ZipFile(zfile, mode='r')
    zlist = zf_class.infolist()
    for i in zlist:
        img = Image.open(ZipFile(zfile, mode='r').open(name=i.filename)).convert('RGB')
        img.show()
#run
show_images('test.zip')

def cv_show_image(img):
        cv.imshow("image", img)
        cv.waitKey(0)
        cv.destroyAllWindows()
#run
#cv_show_image('img.jpg')