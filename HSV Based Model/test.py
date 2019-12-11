from colorextractor import ColorExt
from similar import Similarity
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--index", required = True,
	help = "Path to where the computed index will be stored")
ap.add_argument("-q", "--query", required = True,
	help = "Path to the query image")
ap.add_argument("-r", "--result-path", required = True,
	help = "Path to the result path")
args = vars(ap.parse_args())

cx = ColorExt((8, 12, 3))

query = cv2.imread(args["query"])
features = cx.describe(query)

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