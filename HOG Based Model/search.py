from itertools import chain
from similar import Similarity
import argparse
from hog import Hog_descriptor
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--index", required = True,
	help = "Path to where the computed index will be stored")
ap.add_argument("-q", "--query", required = True,
	help = "Path to the query image")
ap.add_argument("-r", "--result-path", required = True,
	help = "Path to the result path")
args = vars(ap.parse_args())

query = cv2.imread(args["query"], cv2.IMREAD_GRAYSCALE)
hog = Hog_descriptor(query, cell_size=int(16), bin_size=int(8))
features, image = hog.extract()
cv2.imshow('HOG Features',image)
cv2.waitKey(0)
features = list(chain.from_iterable(features))
features.insert(0, len(features))
print("length is",len(features))

searcher = Similarity(args["index"])
results = searcher.search(features)

cv2.imshow("Query", query)
print("Query is: ",query)
cv2.waitKey(0)
print("result is: ",results[0])
# loop over the results
for (score, resultID) in results:
    print("Retrived Logos Are: ", score , "::::::::::" ,resultID )
    result = cv2.imread(args["result_path"] + "/" + resultID)
    img = cv2.imread(resultID,1)
    cv2.imshow('Retrieved Images',img)
    cv2.waitKey(0)