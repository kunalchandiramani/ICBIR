from itertools import chain 
from hog import Hog_descriptor
import argparse
import glob
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", required = True,
	help = "Path to the directory that contains the images to be indexed")
ap.add_argument("-i", "--index", required = True,
	help = "Path to where the computed index will be stored")
args = vars(ap.parse_args()) 

output = open(args["index"], "w")

for imagePath in glob.glob(args["dataset"] + "/*.jpg"):
    imageID = imagePath[imagePath.rfind("/") + 1:]
    img = cv2.imread(imagePath, cv2.IMREAD_GRAYSCALE)
    hog = Hog_descriptor(img, cell_size=int(8), bin_size=int(8))
    vector, image = hog.extract()
    features=vector

    features = list(chain.from_iterable(features))
    features = [str(f) for f in features]
    
    print(len(features))
    
    output.write("%s,%s,%s\n" % (imageID, str(len(features)), ",".join(features)))
    print("%s",imagePath)

output.close()