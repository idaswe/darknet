import glob

FILE = '../cfg/cropped_fox_test.txt'
PNGS = '../data/logo/cropped_fox/test/*.png'

def appendName(filename):
    print(filename)

    textFile.write(filename.replace('..', '.'))
    textFile.write('\n')

if __name__ == '__main__':
    textFile = open(FILE, 'w+')

    for filename in glob.glob(PNGS):
        appendName(filename)

    textFile.close()
