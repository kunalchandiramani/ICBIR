# ICBIR (INTELLIGENT CONTENT BASED IMAGE RETRIEVAL SYSTEM)

The Project is implemented using two different methodologies:
•	Method 01: Color-HSV Based Features- This phase identifies the unique feature vector corresponding to the image features. Hue saturation value (HSV) color space is used for color feature extraction.  
•	Method 02: HOG Based Features-The histogram of oriented gradients (HOG) is a feature descriptor used in computer vision and image processing for the purpose of object detection. The technique counts occurrences of gradient orientation in localized portions of an image.
The dataset can be downloaded from the following link:
http://image.ntua.gr/iva/datasets/flickr_logos/
Instructions for Color-HSV Based Model:
The code is divided into 4 modules:
1.	Colorextractor.py
2.	Index.py
3.	Similar.py
4.	Search.py

1. colorextractor.py	
	In this module, we extract the features of logos. First we divide the image into five parts. For 	each part we calculate the histogram. The histogram is taken from HSV color space. We 	normalize the histogram & return the value. 


2. index.py
	In this module, we index the features in a csv file. We take the path of image dataset & the path 	where the index file will be saved, as an input. Then we process the code & the features are 	saved in the csv file in the form of array.

3. similar.py
In this module, we find the similarity measure. For this we have used chi-squared distance. Here we loop over the rows in the index, parse out the image ID and features, then compute the chi-squared distance between the features in our index and our query features. now that we have distance between the two feature vectors, we can update the results dictionary – the key is the current image ID in the index and the value is the distance we just computed, representing how 'similar' the image in the index is to our query. At last we sort our results, so that the smaller distances i.e. the more relevant images are at the front of the list.

4. search.py
	In this module, first we call all the above mentioned modules. Then we construct the argument 	parser and parse the arguments. We pass csv file, query image & result path to the program as 	an input. We initialize the image descriptor i.e. the no. of bins. Finally we display the query 	image, the exact match image & all other similar images.

Steps to execute the code:
Step 1. First execute colorextractor.py
	>> python colorextractor.py
Step 2: Then execute index.py
	>>  python index.py --dataset dataset --index index.csv
Step 3: Now execute similar.py
	>> python similar.py
Step 4: At last execute search.py
	>> python search.py --index index.csv --query queries/01.jpg --result-path Dataset
  
  
  Instructions for HOG Based Model:

The code is divided into 4 modules:
1.	hog.py
2.	Index.py
3.	Similar.py
4.	Search.py

1.	hog.py
The HOG descriptor focuses on the structure or the shape of an object. In the case of edge features, we only identify if the pixel is an edge or not. HOG provides the edge direction as well. This is done by extracting the gradient and orientation of the edges. Additionally, these orientations are calculated in ‘localized’ portions. This means that the complete image is broken down into smaller regions and for each region, the gradients and orientation  are calculated. Finally the HOG would generate a Histogram for each of these regions separately. The histograms are created using the gradients and orientations of the pixel values, hence the name ‘Histogram of Oriented Gradients’.  The HOG feature descriptor counts the occurrences of gradient orientation in localized portions of an image.
The rest of the files perform steps similar to the steps performed in the 1st Model.

2. index.py
	In this module, we index the features in a csv file. We take the path of image dataset & the path 	where the index file will be saved, as an input. Then we process the code & the features are 	saved in the csv file in the form of array.

3. similar.py
In this module, we find the similarity measure. For this we have used chi-squared distance. Here we loop over the rows in the index, parse out the image ID and features, then compute the chi-squared distance between the features in our index and our query features. now that we have distance between the two feature vectors, we can update the results dictionary – the key is the current image ID in the index and the value is the distance we just computed, representing how 'similar' the image in the index is to our query. At last we sort our results, so that the smaller distances i.e. the more relevant images are at the front of the list.

4. search.py
	In this module, first we call all the above mentioned modules. Then we construct the argument 	parser and parse the arguments. We pass csv file, query image & result path to the program as 	an input. We initialize the image descriptor i.e. the no. of bins. Finally we display the query 	image, the exact match image & all other similar images.

Steps to execute the code:

Step 1. First execute colorextractor.py
	>> python hog.py

Step 2: Then execute index.py
	>>  python index.py --dataset dataset --index index.csv

Step 3: Now execute similar.py
	>> python similar.py

Step 4: At last execute search.py
	>> python search.py --index index.csv  --invoiceSamples/Adidas_invoice.pdf  --result-path Dataset

