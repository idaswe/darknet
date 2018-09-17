from __future__ import division
import os

DIRECTORY = '../data/logo/cropped_fox/test'

def create_txt(filename):
    pathTxt = os.path.join(DIRECTORY, filename.replace('.png','.txt'))
    print(pathTxt)

    height = 100;
    width = 720;

    className = '0'
    # 0,0 reference is in top left corner
    centerX = str(635.5/width)
    centerY = str(34/height)
    objectwidth = str(45/width)
    objectheight = str(20/height)

    string = className + ' ' + centerX + ' ' + centerY + ' ' + objectwidth + ' ' + objectheight
    textFile = open(pathTxt, "w+")
    textFile.write(string)
    textFile.close()

if __name__ == '__main__':
    for filename in os.listdir(DIRECTORY):
        print(filename)
        create_txt(filename)
